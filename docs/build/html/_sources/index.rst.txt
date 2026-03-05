.. mavion-drl-ppo documentation master file, created by
   sphinx-quickstart on Thu Mar  5 14:46:57 2026.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Cruise Control with Proximal Policy Optimization (OpenAI SB3) for MAVION VTOL Platform
============================

Deep Reinforcement Learning (DRL) has shown promising potential for developing controllers capable of handling complex scenarios in the context of Hybrid Aerial Vehicles (HAVs), which combine characteristics of both fixed-wing and rotorcraft dynamics. While DRL offers the
possibility of outperforming traditional methods in highly nonlinear systems operating under uncertain or dynamically changing conditions, its performance and robustness in real-world applications remain active areas of research. In this work, the Proximal Policy Optimization
(PPO) algorithm—implemented via OpenAI’s Stable-Baselines3 library is employed to train policies for cruise control, assuming that trimmed level-flight can be achieved. A custom simulation and training environment was developed using the MAVION platform, a Vertical Take-Off and Landing (VTOL) Unmanned Aerial Vehicle (UAV) designed at ISAE-SUPAERO. Separate two-dimensional (2D) trajectory
controllers were trained for each phase under symmetric flight assumptions, demonstrating accurate tracking of complete flight profiles with minimal error. In addition, generalization techniques were introduced, enabling the trained policies to reliably track unseen target
trajectories within a predefined flight envelope. The performance of the trained controllers was also evaluated under light atmospheric turbulence, showing encouraging results and suggesting potential for robust real-world applications.

**Keywords**: Proximal Policy Optimization (PPO), Unmanned Aerial Vehicle (UAV), Hybrid Aerial Vehicle (HAV), Vertical Take-Off and Landing (VTOL), Deep Reinforcement Learning (DRL), Trajectory Controller

Authors
--------
Vicente ACOSTA (ISAE-SUPAERO, MAE-ASC)
Thibault CLARA (ISAE-SUPAERO, MAE-ASC)

Acknowledgments
---------------
Thank you to Dr. Philippe PASTOR for his support & guidance throughout 2024-206 on these research efforts.

.. toctree::
   :maxdepth: 2
   :caption: Problem Definition

   1-problem-definition/literature-review
   1-problem-definition/mavion-platform
   1-problem-definition/control-problem
