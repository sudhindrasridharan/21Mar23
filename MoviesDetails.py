#!/usr/bin/env python

###########################################################################
#
# - Movies Details Script for Sample
#
# - Movies Details Script perform following Operations:
#   1. Get the total number of movies based on the substring input
#
############################################################################

import os
import sys
import requests

class Movies:

    def __init__(self):
        pass
    def getMoviesDetails(self,substr):
        MoviesdataURL = "https://jsonmock.hackerrank.com/api/moviesdata/search/?Title="+substr

        response = requests.get(MoviesdataURL)
        moviesinfo_dict = response.json()
        print("===========================================================")
        print ("Sub String is", substr )
        print("Status Code is ", response.status_code )
        for moviedetails in moviesinfo_dict['data']:
            print (moviedetails)
        print("Total Number of Movies is: ", len(moviesinfo_dict['data']))
        print("===========================================================")

if __name__ == '__main__':

    objMovies = Movies()
    objMovies.getMoviesDetails("Welcome");
    objMovies.getMoviesDetails("Good");

