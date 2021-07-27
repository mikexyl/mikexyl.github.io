# JDX Robotics Challenge


We won the National Bronze in JDX Robotics Challenge 2017. Held by JD.COM, one of theleading online shopping companies in China, it focused on the industry of smart logistics.
Thechallenge topic we chose is auto-sorting, as the task can be describe as such:

1. Design a robot,to be placed in the center,
2. Recognize and grab boxes in the right semicircle area,
3. Stackthem in the crate in the left semicircle, by their colors and the specified stacking rules.

We designed a robot arm equipped with a air pump and a suction cup to grab boxes, and a Microsoft Kinect for box recognization as shown in pictures.
In detail, firstly we attached an apriltag in the actuator.
And a initialization procedure wouldcontrol it to move along three axis for coordinates calibration automatically.
From the pointclouds, we then were able to extract boxes by removing ground plane and segmentation.
We also masked the depth images by edges detected from color images, to split connected andoverlapped boxes.
A set of distance sensors were utilized for better accuracy of operation and safety.

<div style="text-align:center">
<figure>
  <img src="https://raw.githubusercontent.com/LXYYY/lxyyy.github.io/master/projects/jdx/jdx_drawing.png" alt="drawing" width="400"/>
  <figcaption>Drawings of our JDX auto-sorting robot</figcaption>
</figure>

<figure>
  <img src="https://raw.githubusercontent.com/LXYYY/lxyyy.github.io/master/projects/jdx/jdx_final.jpg" alt="final product" width="400"/>
  <figcaption>picture of our final product</figcaption>
</figure>

<figure>
  <img src="https://raw.githubusercontent.com/LXYYY/lxyyy.github.io/master/projects/jdx/move1.gif" alt="move1" width="400"/>
  <figcaption>JDX robot grabbing boxes</figcaption>
</figure>

<figure>
  <img src="https://raw.githubusercontent.com/LXYYY/lxyyy.github.io/master/projects/jdx/move2.gif" alt="move2" width="400"/>
  <figcaption>JDX robot stacking boxes</figcaption>
</figure>
</div>
