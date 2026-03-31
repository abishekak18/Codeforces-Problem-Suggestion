import requests
import pickle
import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder='static')
CORS(app)

CACHE_FILE = "cf_problems_cache.pkl"

TARGET_TAGS = [
    "math", "dp", "greedy", "graphs", "strings",
    "binary search", "two pointers", "data structures", "bitmasks", "brute_force"
]

def get_all_problems(use_cache=True):
    """Fetch all CF problems, using pickle cache to avoid repeated API hits."""
    if use_cache and os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "rb") as f:
            return pickle.load(f)
    
    prob_url = "https://codeforces.com/api/problemset.problems"
    resp = requests.get(prob_url, timeout=15)
    resp.raise_for_status()
    all_probs = resp.json()['result']['problems']
    
    with open(CACHE_FILE, "wb") as f:
        pickle.dump(all_probs, f)
    
    return all_probs


def get_user_data(user_handle):
    """Fetch user rating and submissions (solved set + skill map)."""
    # 1. Fetch User Info for Rating
    info_url = f"https://codeforces.com/api/user.info?handles={user_handle}"
    info_resp = requests.get(info_url, timeout=15)
    info_resp.raise_for_status()
    user_info = info_resp.json().get('result', [{}])[0]
    current_rating = user_info.get('rating', 800) # Default 800 for unrated

    # 2. Fetch Submissions
    sub_url = f"https://codeforces.com/api/user.status?handle={user_handle}"
    resp = requests.get(sub_url, timeout=15)
    resp.raise_for_status()
    result = resp.json()
    
    if result.get('status') != 'OK':
        raise ValueError(f"Codeforces API error: {result.get('comment', 'Unknown error')}")
    
    submissions = result.get('result', [])
    solved_set = set()
    user_skills = {}
    
    for s in submissions:
        if s.get('verdict') == 'OK':
            prob = s['problem']
            prob_id = f"{prob['contestId']}{prob['index']}"
            solved_set.add(prob_id)
            for tag in prob.get('tags', []):
                user_skills[tag] = user_skills.get(tag, 0) + 1
    
    return solved_set, user_skills, current_rating


def get_categorized_recommendations(user_handle, target_tags, refresh_cache=False):
    solved_set, user_skills, current_rating = get_user_data(user_handle)
    all_probs = get_all_problems(use_cache=not refresh_cache)

    categorized_recs = {tag: [] for tag in target_tags}
    
    # Range Calculation
    lower_bound = current_rating - 200
    upper_bound = current_rating + 200

    for prob in all_probs:
        prob_id = f"{prob['contestId']}{prob.get('index', '')}"
        rating = prob.get('rating')

        # FILTERING LOGIC
        if prob_id in solved_set:
            continue
        
        # Skip problems without ratings or those outside the +/- 200 range
        if rating is None or not (lower_bound <= rating <= upper_bound):
            continue

        p_tags = prob.get('tags', [])
        score = sum(user_skills.get(t, 0) for t in p_tags)

        for tag in target_tags:
            if tag in p_tags:
                categorized_recs[tag].append({
                    'name': prob['name'],
                    'contestId': prob['contestId'],
                    'index': prob['index'],
                    'url': f"https://codeforces.com/contest/{prob['contestId']}/problem/{prob['index']}",
                    'score': score,
                    'rating': rating,
                    'tags': p_tags
                })

    final_output = {}
    for tag in target_tags:
        # Sort by user skill score (matching what you had)
        sorted_list = sorted(categorized_recs[tag], key=lambda x: x['score'], reverse=True)
        final_output[tag] = sorted_list[:5]

    return final_output, len(solved_set), current_rating


@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


@app.route('/api/recommend', methods=['GET'])
def recommend():
    handle = request.args.get('handle', '').strip()
    refresh = request.args.get('refresh', 'false').lower() == 'true'

    if not handle:
        return jsonify({'error': 'Please provide a Codeforces handle.'}), 400

    try:
        results, solved_count, current_rating = get_categorized_recommendations(handle, TARGET_TAGS, refresh_cache=refresh)
        return jsonify({
            'handle': handle,
            'current_rating': current_rating,
            'solved_count': solved_count,
            'recommendations': results,
            'tags': TARGET_TAGS
        })
    except requests.exceptions.HTTPError:
        return jsonify({'error': f'User "{handle}" not found on Codeforces.'}), 404
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'Something went wrong: {str(e)}'}), 500


@app.route('/api/cache/clear', methods=['POST'])
def clear_cache():
    if os.path.exists(CACHE_FILE):
        os.remove(CACHE_FILE)
        return jsonify({'message': 'Cache cleared.'})
    return jsonify({'message': 'No cache to clear.'})


if __name__ == '__main__':
    # It is recommended to clear cache once if ratings seem missing
    app.run(debug=True, port=5000)