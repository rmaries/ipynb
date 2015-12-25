#!/usr/bin/python
class Time:
    def whatTime(self, seconds):
        s = seconds%60
        minutes = seconds/60
        if minutes > 60:
            minutes
        hours = minutes/60
        return str(hours)+":"+str(minutes)+":"+str(s)
#print Time.whatTime(0)
t =  Time()
print t.whatTime(3661)
