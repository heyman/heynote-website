download_releases:
	mkdir -p download
	gh api /repos/heyman/heynote/releases > download/releases.json
	curl 'https://raw.githubusercontent.com/heyman/heynote/main/docs/index.md' > download/docs.md
	gh api \
		--method POST \
		-H "Accept: application/vnd.github+json" \
		-H "X-GitHub-Api-Version: 2022-11-28" \
		/markdown \
		-f "text=$$(cat download/docs.md)" > download/docs.html




generate:
	rm -rf ./_site
	mkdir ./_site
	cp -r ./img ./_site/img
	cp -r ./js ./_site/js
	sass css/style.sass ./_site/css/style.css
	cp css/github-markdown.css ./_site/css/github-markdown.css
	python generate.py
