# RoboMasters National University Robotics Competition

In 2015/2016, our team won the national champion of [RoboMasters](https://www.robomaster.com/en-US), which is an exciting and competitive robot battle competition series held by DJI and MoE of China.
Our team of 15 undergraduates are required to design a series of robots attacking opponents, including 4 models of ground robots, one drone and their necessary standby duplicates.
My group was responsable for building our UAV to accomplish a set of tasks:

- Grab golf balls from the parking apron,
- Automatically fly to the enemy area,
- Recognise opponent robots and airdrop balls.

We built our UAV based on a [DJI M100 Quadcopter](https://www.dji.com/sg/matrice100).
A lightweight parallel manipulator is designed and attached to our drone to grab and drop balls, which was patented after the competition.
Our competition UAV and its manipulator:

<div style="text-align:center">
<figure>
<img src="https://raw.githubusercontent.com/LXYYY/lxyyy.github.io/master/projects/rm/M100.png" alt="drawing" width="400"/>
  <figcaption>Drawings of our RoboMasters UAV</figcaption>
</figure>
<figure>
<img src="https://raw.githubusercontent.com/LXYYY/lxyyy.github.io/master/projects/rm/arm_patent.png" alt="parallel manipulator" width="400"/>
  <figcaption>Drawings of our manipulator</figcaption>
</figure>
</div>


To effectively track opponent robots, We developed an image preprocessing algorithm and robot recognisation classifier, tuned specifically for the illumination condition and item setup in the venue.
Meanwhile to meet the max weight of 4kg of the entire UAV, we designed a lightweight onboard parallel manipulator driven by 3 servos, with a cylinder ball trap mounted.
After our effective weight optimization, the final model weights only 600g, without damaging its functionality.
Having springs in the cylinder surface, this ball trap was able to squeeze in the balls, and a double-layered rotatable bottom allows to drop the balls when opponents are detected.

As last, we achieved the highest ball catching efficiency in competition and effective recognization and airdropping in lab environment.

<div style="text-align:center">
<figure>
<img src="https://raw.githubusercontent.com/LXYYY/lxyyy.github.io/master/projects/rm/IMG_0453.GIF" alt="grabbing balls" width="400"/>
  <figcaption>UAV grabbing balls</figcaption>
</figure>
<figure>
<img src="https://raw.githubusercontent.com/LXYYY/lxyyy.github.io/master/projects/rm/IMG_0454.GIF" alt="dropping" width="400"/>
  <figcaption>UAV dropping balls</figcaption>
</figure>
</div>