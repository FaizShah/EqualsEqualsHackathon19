
from recognition import foodScan
from data_extraction import data_extraction
#name = foodScan('https://drive.google.com/file/d/18LNMzNuknRwrXoAnzzpW6k9Rec6tt8DA/view?usp=sharing')

descrip = foodScan('apple1.jpg')
data_extraction(descrip)