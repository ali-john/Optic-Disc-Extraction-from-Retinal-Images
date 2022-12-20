# Optic-Disc-Extraction-from-Retinal-Images
 ---
 
 ## Introduction:
 
 In this work I devised a new technique for optic disc extraction from retinal images using Spatial enhancements and connected component labelling. The algorithm I devised is:
 - Apply Contrast stretching to grayscale retinal image keeping only top 3% data points.
 - Apply max filter to output of step 1 in iterative fashion to merge small regions into larger ones.
 - Apply thresholding to image keeping threshold at grayscale value of 90. This gives binary image.
 - Apply CCA to binary image. This gives all potential candidates for optic disc.
 - Map given retinal blood vessels map to possible optic disc candidates and look for region with maximum blood vessels.
 - This region is your optic disc.
 - Calculate center of optic disc region and circle boundary of optic disc on input image.
 
 
 ## Implementation & Algorithm Explanantion:
 
 The input is a retinal image scan lets take one sample image.
 
 

 <img src="https://user-images.githubusercontent.com/63426759/208633565-956ec1ee-d70e-42ab-9907-b3282e4f5983.png" width="300" height="300">
 
 Then the input image is passed to transform function where contrast stretching and max filter is applied. This changes the input retinal image in form where further steps can be applied:
 
 
<img src="https://user-images.githubusercontent.com/63426759/208634080-b93a8ca9-d6d7-4a07-83a6-a50b47e1d393.png" width="300" height="300">




Now the transformed image is passed to CCA function where first thresholding is performed to convert image to binary and after that CCA is applied. This gives colored candidates for optic disc:


<img src="https://user-images.githubusercontent.com/63426759/208634374-eb8e18e2-ba1a-4d4d-9c5e-da53900c52af.png" width="300" height="300">

Now CCA labelled image along with blood vessels map is passed to another function where blood vessels map is used to find true optic disc amongst all candidates for optic disc. After identifying true optic disc, its center is calculated and then a circle is drawn on input image highlighting the boundaries for optic disc.



<img src="https://user-images.githubusercontent.com/63426759/208634835-ae22bca1-820d-4870-975e-39688d625af3.png" width="500" height="300">

Marking boundaries of optic disc region:


<img src="https://user-images.githubusercontent.com/63426759/208635220-9478fa28-e870-4a90-a359-80a290f88d1d.png" width="500" height="300">


## Results:
 ---
 
The results on some of data samples are shown:


<img src="https://user-images.githubusercontent.com/63426759/208635623-2b6ccc36-a734-43b9-958d-dcb84a55861a.png" width="500" height="300">


<img src="https://user-images.githubusercontent.com/63426759/208635994-a51fd98e-3c9b-4c8c-964a-e23e6b960607.png" width="500" height="300">


<img src="https://user-images.githubusercontent.com/63426759/208636126-6f57dcba-597d-4d41-ad20-6e68a2c84746.png" width="500" height="300">


<img src="https://user-images.githubusercontent.com/63426759/208636363-af5b3b3c-82a0-48db-904e-69c4d7692890.png" width="500" height="300">
