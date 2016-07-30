from datetime import timedelta,datetime
import datetime as d
import operator
from event import Event
from slot import Slot

class ConferenceManager():
    """
    / **
      * 1. Read data from file and create a list of Event objects from strings.
      * 2. sort the list of Events.
      * 3. find out the combination for morning session
      * 4. find out the combination for evening sessions (180 >= totalSessionTime <= 240).
      * 5. check if any task remaining in the list if yes then try to fill all the eve session. 
      * 6. Will not have any task duration more than 240 mins i.e, evening session
      */
    """

    morning=[]#morning schedule
    evening=[]#evening schedule
    perday=7*60
    
    def __init__(self,file):
        #list of talk events
        self.talk_list = self.readInput(file)
    
    def totaltime(self,talk_list):
        """Calculate the maximum days required for confrence schedulelist
        talk_list is a list of talk events"""
        return sum([event.duration for event in talk_list])

    def readInput(self,file):
        """Read the input file and storing as event object"""
        talks = []
        with open(file) as f:
            for line in f:
                title, minutes = line.rsplit(maxsplit=1)
                try:
                    minutes = int(minutes[:-3])
                # negative indexing raises error, so it means it's lightning
                except ValueError:
                    minutes = 5
                event=Event(line,minutes)
                talks.append(event)
        return talks

    def clear(self,slot_list):
        """Clear scheduled events from a list"""
        for event_list in slot_list:
            for event in event_list:
                self.talk_list.remove(event)

    def schedule(self,talk_list):
        """Schedule events for a list of events"""
        totaltime=self.totaltime(talk_list)
        possibledays=int(totaltime/self.perday)+1
        talk_list.sort(key=operator.attrgetter('duration'))
        m=self.combinations(talk_list,possibledays,Slot(3*60))#morning slot
        self.clear(m)
        evening_slot=Slot(4*60,3*60)
        e=self.combinations(talk_list,possibledays,evening_slot)#morning slot
        self.clear(e)

        #fill remaining events in evening slot 
        if(self.talk_list):
            for event_list in e:
                totaltime=self.totaltime(event_list)
                for event in self.talk_list:
                    if event.duration+totaltime<=evening_slot.max:
                        event_list.append(event)
                        event.scheduled=True
                        self.talk_list.remove(event)

                if not self.talk_list:
                    break

        self.morning=m
        self.evening=e

    def combinations(self,event_list,possibledays,slot):
        list_size=len(event_list)
        e=[]
        count=0
        for i in range(list_size):
            start=i
            totaltime=0
            comb=[]
            while(start is not list_size):
                curr=start
                start+=1
                event=event_list[curr]
                if event.scheduled or not slot.isValidEvent(event,totaltime):
                    continue

                comb.append(event)
                totaltime+=event.duration
                if totaltime>=slot.max:
                    break
          
            if slot.isValidSession(totaltime):
                e.append(comb)
                for talk in comb:
                    talk.scheduled=True
                count+=1
                if count==possibledays:
                    break

        return e

    def print_output(self):
        format="%I:%M %p"
        out=''
        for day in range(len(self.morning)):
            date = datetime(1,1,1,hour=9)
            out+="Track " + str(day+1) + ":"+"\n"
            for event in self.morning[day]:
                out+=date.strftime(format)+" "+event.name+"\n"
                date=date+d.timedelta(minutes=event.duration)

            date=date
            out+=date.strftime(format)+ " Lunch"+"\n"
            date=date+d.timedelta(minutes=60)

            try:#to handle cases where morning session has extra session and no evening session
                for event in self.evening[day]:
                    out+=date.strftime(format)+" "+event.name+"\n"
                    date=date+d.timedelta(minutes=event.duration)
            except:
                pass

            if(date<=datetime(1,1,1,hour=16)):
                date=datetime.min+d.timedelta(hours=16)
            else:
                date=datetime.min+d.timedelta(hours=17)
            out+=date.strftime(format)+ " Network"+"\n"
            
        print(out)


