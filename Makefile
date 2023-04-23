lint :
	isort .
	black .

commit : 
	git add .
	git commit -m 'commit from make file'
	git push origin master
