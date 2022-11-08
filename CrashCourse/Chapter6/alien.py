alien_0 = {'color': 'blue', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"I just earned {new_points} points")

alien_0['x_position'] = 0
alien_0['y_position'] = 30
alien_0['z_position'] = -2

print(alien_0)

#Starting with an Empty Dictionary

alien_23 = {}
alien_23['color'] = 'cyan'
alien_23['points'] = 10

print(alien_23)


#Modifying Values in a Dictionary
alien_24 = {'color': 'yellow'}
print(f"The alien is {alien_24['color']}")

alien_24 = {'color': 'white'}
print(f"The alien is now {alien_24['color']}")


alien_25 = {'x_position': 0, 'y_position': 0, 'z_position': 0, 'speed': 'normal'}
x_position = alien_25['x_position']
y_position = alien_25['y_position']
z_position = alien_25['z_position']
print(f"The original position: (x={x_position}, y={y_position}, z={z_position})")

if alien_25['speed'] == 'fast':
    alien_25['x_position'] += 2
    alien_25['y_position'] += 3
    alien_25['z_position'] += 4
elif alien_25['speed'] == 'normal':
    alien_25['x_position'] += 1
    alien_25['y_position'] += 1
    alien_25['z_position'] += 1
else:
    alien_25['x_position'] += 0.1
    alien_25['y_position'] += 0.2
    alien_25['z_position'] += 0.3

x_position = alien_25['x_position']
y_position = alien_25['y_position']
z_position = alien_25['z_position']
print(f"New position: (x={x_position}, y={y_position}, z={z_position})")




