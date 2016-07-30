from schedule import ConferenceManager

c = ConferenceManager('test.txt')
c.schedule(c.talk_list)
print(c.morning)
c.print_output()