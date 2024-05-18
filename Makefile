default:
	cat Makefile


screenshots:
	@./make-screenshots.sh


screenshots-clear:
	find {0,1,2,3,4,5,6,7,8,9}* -name "*.png" -exec rm {} \;
	
	