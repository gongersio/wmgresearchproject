**This repository contains all the code relating to my research project under grant from Warwick Manufacturing Group (WMG).**

The research title was: ***Factors Affecting the Popularity of VR-Related Educational Videos on TikTok***

The data collection stage involved identifying relevant videos using general keyword search terms (e.g. *virtual reality learning*), and then manually downloading this set of videos from the TikTok website.

Contact me (**samaksh.agarwal@warwick.ac.uk**) if you would like access to the complete dataset.

The speech and video content of these videos was then analysed through a data pipeline implemented in Python.

The speech/text analysis pipeline for each video included the following stages:
* Video Transcription (using the *pydub* and *speech_recognition* libraries)
* Punctuation Restoration (using the *rpunct* library)
* Keyword Extraction (using the *yake* library)

FFmpeg (required for video transcription) can be downloaded here: https://ffmpeg.org/download.html

Furthermore, the transitions in each video were analysed in order to record the number of distinct scenes and calculate the average scene length (this was done using the *pyscenedetect* library).

Further statistical analysis and data visualisation was performed using dedicated libraries such as *pandas*, *NumPy*, and *matplotlib*.

Using the results of this data analysis, an academic research paper was written. The paper was accepted by the AIKIEE-2023 conference and has now been published in the IEEE Xplore Digital Library.

The final paper can be found at: 
*  https://ieeexplore.ieee.org/document/10390456 (official link)
* https://drive.google.com/file/d/12nb_i909t0K-BJZQlK7t7mSTReOGsj9s/ (free link)
