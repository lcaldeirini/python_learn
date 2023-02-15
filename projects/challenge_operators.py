# Logic operation 


work_tuesday = True 
work_thursday = False

tv_50 = work_tuesday and work_thursday
bonus = work_tuesday or work_thursday
tv_32 = work_tuesday != work_thursday
health = not bonus

print("tv_50={} tv_32={} bonus={} health={}"
    .format (tv_50, tv_32, bonus, health))


