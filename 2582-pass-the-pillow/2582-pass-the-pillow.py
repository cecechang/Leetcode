class Solution(object):
    def passThePillow(self, n, time):
        people_list = [x for x in range(1, n+1)]
        people_list.extend(people_list[-2:0:-1])
        while time >= len(people_list):
            time = time - len(people_list)
        return people_list[time]