# Github_user_analysis
Github-user's data: Get and Analyze :bar_chart: :bar_chart: :bar_chart:

Github provide a powerful API that make developers can interact easily with its own data. In this repository, we use github-api to get user's data, by analyzing them, we can understand more about user's coding strength and coding behaviors.

## Ver 1: on jupyter notebook :heavy_check_mark:

(Chart were plotted by **plotly** can't display in github's jupyter notebook. In order to view, you can download [notebook](https://github.com/damminhtien/Github_user_analysis/blob/master/Github_user_analysis.ipynb) > change **password** and **target_user** variable > run locally)

Some features:

Most Common Languages:

![most_common_languages](https://github.com/damminhtien/Github_user_analysis/blob/master/most_common_languages.png)
<br/>

Stars per repository: :heavy_check_mark:

![star_per_repo](https://github.com/damminhtien/Github_user_analysis/blob/master/star_per_repo.png)
<br/>

Commits per repository: :heavy_check_mark:

![commit_per_repo](https://github.com/damminhtien/Github_user_analysis/blob/master/commit_per_repo.png)
<br/>

Commits per year: :heavy_check_mark:

![commit_per_year](https://github.com/damminhtien/Github_user_analysis/blob/master/commit_per_year.png)
<br/>

Commits per month: :heavy_check_mark:

![commit_per_month](https://github.com/damminhtien/Github_user_analysis/blob/master/commit_per_month.png)

## Ver 2: on web :heavy_check_mark:
1. Install neccessary packages
```bash
pip install requirements.txt
```
2. Set your password in setting.py file

3. Start Flask server
```bash
python app.py
```
or
```bash
gunicorn app:app
```

4. Open browser and enjoy~

See me: [localhost:5000](localhost:5000)

See specific user: [localhost:5000/user/<user-name>](localhost:5000/user/torvalds)
