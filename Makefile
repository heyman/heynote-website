download_releases:
	gh api /repos/heyman/heynote/releases > releases.json

generate:
	rm -rf ./_site
	mkdir ./_site
	cp -r ./img ./_site/img
	cp -r ./js ./_site/js
	sass css/style.sass ./_site/css/style.css
	python generate.py
