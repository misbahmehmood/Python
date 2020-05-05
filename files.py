file=open('teams.txt', 'w')
lines= ('first team\n second team\n thrid team\n fourth team\n fifth team')
file.write(lines)
file.close()

file=open('teams.txt', 'r')
print(file.readline())
file.readline()
file.readline()
print(file.readline())
file.readline()
file.close()


