
from hashlib import sha1
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

sessions = AudioUtilities.GetAllSessions()





def getAudioControllers():
   controllers = [];
   for session in sessions:
      controllers.append([session.__str__(), sha1(session.__str__().encode()).hexdigest(), session._ctl.QueryInterface(ISimpleAudioVolume).GetMasterVolume(), session._ctl.QueryInterface(ISimpleAudioVolume).GetMute()]);
   return controllers;



def changeControllerVolume(controller, volume):
   for session in sessions:
      if session.__str__() == controller:
         session._ctl.QueryInterface(ISimpleAudioVolume).SetMasterVolume(float(volume), None);
         break;




def muteUnmute(controller):
   status = "unmuted";
   for session in sessions:
      if session.__str__() == controller:
         if session._ctl.QueryInterface(ISimpleAudioVolume).GetMute() == 1:
            session._ctl.QueryInterface(ISimpleAudioVolume).SetMute(0,  None);
         else:
            session._ctl.QueryInterface(ISimpleAudioVolume).SetMute(1,  None);
            status = "muted";
         break;
   return status;