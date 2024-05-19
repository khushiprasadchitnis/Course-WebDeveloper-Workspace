default:
	cat Makefile


screenshots:
	@./bin/make-screenshots.sh 01_html_css


screenshots-clear:
	find {0,1,2,3,4,5,6,7,8,9}* -name "*.png" -exec rm {} \;
	
	
