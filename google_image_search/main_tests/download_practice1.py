# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 19:17:19 2018

@author: project_X
"""

from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"Polar bears,baloons,Beaches","limit":20,"print_urls":True}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths) 