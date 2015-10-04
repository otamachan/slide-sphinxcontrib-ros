すごいノード
============

ノードAPI
---------

.. ros:node:: my_great_package/GreateNode

   :pub geometry_msgs/Vector3 ~pos: position of the robot

   :sub geometry_msgs/Twist ~vel: reference velocity

   :srv  std_srvs/Trigger ~trigger: trigger for start

   :srv_called std_srvs/Empty ~beep: beep service

   :action control_msgs/GripperCommand ~gripper: gripper action of the robot

   :action_called moveit_msgs/Pickup ~pickup: pickup action

   :param int32 clients: number of clients
   :param-default clients: 10

   :param_set int32 motors: number of motors

   これはすごいノードです。
