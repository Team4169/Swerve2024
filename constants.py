#
# The constants module is a convenience place for teams to hold robot-wide
# numerical or boolean RobotConstants. Don't use this for any other purpose!
#

import math
import wpiutil
import UtilCommands
from wpimath.kinematics import SwerveDrive4Kinematics
from wpimath.geometry._geometry import Translation2d, Pose2d
from wpimath.trajectory import TrapezoidProfileRadians, TrapezoidProfile

#~ Field Measurements/targets
class FildConstants:
    kFieldWidth = UtilCommands.inchesToMeters(27) #2023 charged up change next year
    kFieldLength = UtilCommands.inchesToMeters(54)

#~ Controller Options
class OIConstants:
    kDriverControllerPort = 0
    kArmControllerPort = 1
    deadzone = .12 

#~ robot specifications
class RobotConstants:
        
    kWheelDiameterMeters = UtilCommands.inchesToMeters(4) #^ wheele listed as "Wheel, Billet, 4"OD x 1.5"W (MK4/4i)"" I think that's what the 4 OD means

    kTrackWidth = UtilCommands.inchesToMeters(20) #found with measuring tape
        # ? Distance between the right and left wheels
    kWheelBase = UtilCommands.inchesToMeters(20) #todo: find the actual wheel base
        # ? Distance between the front and back wheels
    kDriveKinematics = SwerveDrive4Kinematics(
        Translation2d(-kTrackWidth / 2, -kWheelBase / 2), #Front Left       
        Translation2d(kTrackWidth / 2, -kWheelBase / 2), #Front Right
        Translation2d(-kTrackWidth / 2, kWheelBase / 2), #Back Left
        Translation2d(kTrackWidth / 2, kWheelBase / 2), #Back Right

        # ? location of each swerve module relative to the center of the robot
    )
    kFrontLeftWheelPosition = Translation2d(kTrackWidth / 2, kWheelBase / 2)
    kFrontRightWheelPosition = Translation2d(kTrackWidth / 2, -kWheelBase / 2)
    kBackLeftWheelPosition = Translation2d(kTrackWidth / 2, -kWheelBase / 2)
    kBackRightWheelPosition = Translation2d(-kTrackWidth / 2, -kWheelBase / 2)


    frontLeftDrivingMotorID = 1
    frontLeftTurningMotorID = 11
    frontLeftDrivingMotorReversed = True
    frontLeftTurningMotorReversed = False
    frontLeftAbsoluteEncoderId = 1 #DIO port ID
    frontLeftAbsoluteEncoderOffset = .5 * math.pi -.728
    frontLeftAbsoluteEncoderReversed = True

    frontRightDrivingMotorID = 2
    frontRightTurningMotorID = 22
    frontRightDrivingMotorReversed = True
    frontRightTurningMotorReversed = False
    frontRightAbsoluteEncoderId = 2
    frontRightAbsoluteEncoderOffset = 2 * math.pi
    frontRightAbsoluteEncoderReversed = True

    backRightDrivingMotorID = 3
    backRightTurningMotorID = 33
    backRightDrivingMotorReversed = True
    backRightTurningMotorReversed = False 
    backRightAbsoluteEncoderId = 3
    backRightAbsoluteEncoderOffset = .25#.25
    backRightAbsoluteEncoderReversed = True
    
    backLeftDrivingMotorID = 4
    backLeftTurningMotorID = 44
    backLeftDrivingMotorReversed = True
    backLeftTurningMotorReversed = False
    backLeftAbsoluteEncoderId = 4
    backLeftAbsoluteEncoderOffset = 5.571
    backLeftAbsoluteEncoderReversed = True

    
    
    #what is the fastest speed laterally our robot can go
    kphysicalMaxSpeedMetersPerSecond = 1.165 * 2 #! Find through test current is test based on 1/2 speeds
    #or maybethrough the max rpm of motors 
    #what is the fastest speed  rotationally our robot can go
    kPhysicalMaxAngularSpeedRadiansPerSecond  = kphysicalMaxSpeedMetersPerSecond * 2 / kWheelDiameterMeters #! Find through Current UNKNOWN
    
    kTeleopDriveMaxAccelerationMetersPerSecSquared = 3 #* Found through .5 test, should be the same no matter the power
    kTeleopDriveMaxAngularAccelerationRadiansPerSecSquared = kTeleopDriveMaxAccelerationMetersPerSecSquared * 2 / kWheelDiameterMeters

    #what is the max speed we allow teleop driver to move laterally
    kTeleopDriveMaxSpeedMetersPerSecond = kphysicalMaxSpeedMetersPerSecond / 2 # the /2 is the restriction we want to put on speed
    kTeleopDriveMaxAngularSpeedRadiansPerSecond = kPhysicalMaxAngularSpeedRadiansPerSecond / 2

    

# ~ Swerve Constants 


#todo Change above
class ModuleConstants:
    kWheelDiameterMeters = UtilCommands.inchesToMeters(4) #^ wheele listed as "Wheel, Billet, 4"OD x 1.5"W (MK4/4i)"" I think that's what the 4 OD means

    kDriveMotorGearRatio = 1/6.75 
    kTurningMotorGearRatio = 1/13.3714 #*found through wcp site https://docs.wcproducts.com/wcp-swervex/general-info/ratio-options#:~:text=35%3A1%20or-,13.3714,-%3A1

    kDrivingEncoderRot2Meter = kDriveMotorGearRatio * math.pi * kWheelDiameterMeters
    KDrivingEncoderRPM2MeterPerSec = kDrivingEncoderRot2Meter / 60 #* Initially in RPM, converted to Mps

    kWheelDistancePerRadian = kDrivingEncoderRot2Meter / (2 * math.pi)

    kTurningEncoderRot2Rad = kTurningMotorGearRatio * 2 * math.pi
    kTurningEncoderRPM2RadPerSec = kTurningEncoderRot2Rad / 60 

    kPTurning = .2 #? turning PID controller per wheel


# ~ Auto Constants

class AutoConstants:
        kMaxSpeedMetersPerSecond = RobotConstants.kphysicalMaxSpeedMetersPerSecond / 4
        kMaxAccelerationMetersPerSecondSquared = 3
        kMaxAngularAccelerationRadiansPerSecondSquared = math.pi / 4

        kPXController = 1.0
        kPYController = 1.0

        kMaxAngularSpeedRadiansPerSecond = RobotConstants.kphysicalMaxSpeedMetersPerSecond / 10

        kPThetaController = 1.0
        kThetaControllerConstraints = TrapezoidProfileRadians.Constraints(
                kMaxAngularSpeedRadiansPerSecond,
                kMaxAngularAccelerationRadiansPerSecondSquared,
        )
class sim:
    kSimTargetName = "SimTarget"
    # kSimDefaultTargetLocation = Pose2d(
    #     kFieldLength / 2, kFieldWidth / 2, 180 * kRadiansPerDegree
    # )
    """[meters, meters, radians]"""

    kSimDefaultRobotLocation = Pose2d(FildConstants.kFieldLength / 2, FildConstants.kFieldWidth / 2, 0)
    # kSimDefaultTargetHeight = 8 * kMetersPerFoot + 8 * kMetersPerInch  # 8ft 8in
    # kSimBallName = "SimBall"
    # kSimDefaultBallLocation = Pose2d(kFieldLength / 4, kFieldWidth / 2, 0)

    """meters"""

    kSimRobotPoseArrayKey = "SimRobotPoseArray"
    kSimTargetPoseArrayKey = "SimTargetPoseArray"
    kSimBallPoseArrayKey = "SimBallPoseArray"
    kSimTargetHeightKey = "SimTargetHeight"
    kSimTargetTrackingModuleName = "sim_target_tracker"
    kSimTargetUpperHubRadius = 2

    kSimFrontLeftDriveMotorPort = 0
    kSimFrontLeftSteerMotorPort = 1
    kSimFrontRightDriveMotorPort = 2
    kSimFrontRightSteerMotorPort = 3
    kSimBackLeftDriveMotorPort = 4
    kSimBackLeftSteerMotorPort = 5
    kSimBackRightDriveMotorPort = 6
    kSimBackRightSteerMotorPort = 7


    kSimFrontLeftDriveEncoderPorts = (16, 1)
    kSimFrontLeftSteerEncoderPorts = (2, 3)
    kSimFrontRightDriveEncoderPorts = (4, 5)
    kSimFrontRightSteerEncoderPorts = (6, 7)
    kSimBackLeftDriveEncoderPorts = (8, 9)
    kSimBackLeftSteerEncoderPorts = (10, 11)
    kSimBackRightDriveEncoderPorts = (12, 13)
    kSimBackRightSteerEncoderPorts = (14, 15)
