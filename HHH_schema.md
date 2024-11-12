## Brain Stormed HHH Database Schema

### Riders Table

- Stores information about each rider registered for the race.

```sql
CREATE TABLE riders (
rider_id INT AUTO_INCREMENT PRIMARY KEY,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
gender ENUM('Male', 'Female', 'Non-binary', 'Other'),
age INT NOT NULL,
email VARCHAR(100) UNIQUE,
phone_number VARCHAR(15),
address VARCHAR(255),
emergency_contact_name VARCHAR(100),
emergency_contact_phone VARCHAR(15),
registration_date DATE DEFAULT CURRENT_DATE,
category VARCHAR(50), -- E.g., "Amateur", "Pro", "Youth", etc.
team_name VARCHAR(100) -- If riders are grouped in teams
);

```

### Volunteers Table

- Stores information about each volunteer, including contact information and roles.

```sql
CREATE TABLE volunteers (
volunteer_id INT AUTO_INCREMENT PRIMARY KEY,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
email VARCHAR(100) UNIQUE,
phone_number VARCHAR(15),
address VARCHAR(255),
role VARCHAR(100), -- E.g., "Race Marshal", "Water Station", "Registration"
assigned_to_checkpoint INT, -- References checkpoints if needed
start_date DATE,
end_date DATE
);

```

### Race Events Table

- Tracks individual races or events (e.g., a race series or multiple heats).

```sql
CREATE TABLE race_events (
event_id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100) NOT NULL,
date DATE NOT NULL,
start_time TIME,
end_time TIME,
location VARCHAR(255),
description TEXT,
max_participants INT,
registration_fee DECIMAL(10, 2)
);

```

### Race Registrations Table

- Tracks which riders are registered for which events.

```sql
CREATE TABLE race_registrations (
registration_id INT AUTO_INCREMENT PRIMARY KEY,
rider_id INT NOT NULL,
event_id INT NOT NULL,
registration_date DATE DEFAULT CURRENT_DATE,
payment_status ENUM('Paid', 'Pending', 'Cancelled'),
FOREIGN KEY (rider_id) REFERENCES riders(rider_id),
FOREIGN KEY (event_id) REFERENCES race_events(event_id)
);

```

### Volunteer Assignments Table

- Links volunteers to specific events, roles, or checkpoints.

```sql
CREATE TABLE volunteer_assignments (
assignment_id INT AUTO_INCREMENT PRIMARY KEY,
volunteer_id INT NOT NULL,
event_id INT,
role VARCHAR(100),
checkpoint_number INT, -- Checkpoints or specific locations
shift_start TIME,
shift_end TIME,
FOREIGN KEY (volunteer_id) REFERENCES volunteers(volunteer_id),
FOREIGN KEY (event_id) REFERENCES race_events(event_id)
);

```

### Race Results Table

- Stores the race completion details and rankings for each rider.

```sql
CREATE TABLE race_results (
result_id INT AUTO_INCREMENT PRIMARY KEY,
event_id INT NOT NULL,
rider_id INT NOT NULL,
finish_time TIME,
ranking INT, -- Position the rider finished in
penalties INT DEFAULT 0, -- Time penalties (in seconds)
final_time TIME AS (finish_time + INTERVAL penalties SECOND) PERSISTENT,
FOREIGN KEY (event_id) REFERENCES race_events(event_id),
FOREIGN KEY (rider_id) REFERENCES riders(rider_id)
);

```

### Checkpoints Table

- If the race has multiple checkpoints or locations, this table can help track details per checkpoint.

```sql
CREATE TABLE checkpoints (
checkpoint_id INT AUTO_INCREMENT PRIMARY KEY,
event_id INT NOT NULL,
location_name VARCHAR(100),
latitude DECIMAL(10, 8),
longitude DECIMAL(11, 8),
checkpoint_order INT, -- Order in the race route
FOREIGN KEY (event_id) REFERENCES race_events(event_id)
);

```

### Team Table (Optional)

- If riders can participate as teams, this table will manage team information.

```sql
CREATE TABLE teams (
team_id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100) NOT NULL UNIQUE,
manager_name VARCHAR(100),
manager_contact VARCHAR(15),
sponsor VARCHAR(100),
FOREIGN KEY (team_id) REFERENCES riders(rider_id) -- Optional team leader or primary contact
);

```

### Team Membership Table (Optional)

- If riders are assigned to teams, this table links them to their respective teams.

```sql
CREATE TABLE team_memberships (
membership_id INT AUTO_INCREMENT PRIMARY KEY,
rider_id INT NOT NULL,
team_id INT NOT NULL,
role VARCHAR(50), -- E.g., "Leader", "Support"
FOREIGN KEY (rider_id) REFERENCES riders(rider_id),
FOREIGN KEY (team_id) REFERENCES teams(team_id)
);

```

###  Race Notifications Table (Optional)

- If you want to notify riders and volunteers about changes, this table can store notification details.

```sql
CREATE TABLE notifications (
notification_id INT AUTO_INCREMENT PRIMARY KEY,
recipient_id INT NOT NULL, -- Can be either rider_id or volunteer_id
recipient_type ENUM('Rider', 'Volunteer'),
event_id INT,
message TEXT,
sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (event_id) REFERENCES race_events(event_id)
);

```

## Relationships

    •	One-to-Many:
    •	riders to race_registrations (one rider can register for many events).
    •	race_events to race_results (each event has many results).
    •	race_events to volunteer_assignments (each event can have many volunteer assignments).
    •	teams to team_memberships (each team can have multiple riders).
    •	Many-to-Many:
    •	race_events and riders through race_registrations.
    •	teams and riders through team_memberships.

## Indexing Suggestions

    •	Indexes on Foreign Keys: Add indexes on foreign key columns (e.g., rider_id in race_registrations) to speed up joins.
    •	Unique Constraints: Use unique constraints where applicable (e.g., email in riders and volunteers).
    •	Search and Filtering: Consider adding indexes on frequently searched fields, like event_id in race_results.

Summary

This schema provides flexibility to manage:
- Rider and Volunteer Information: Basic contact and role-related details.
- Event Management: Track multiple race events with unique settings and capacities.
- Team and Registration: Handle team-based registrations if needed.
- Race Results and Rankings: Store each rider’s results and calculate final times, including penalties.
- Notifications: Optional feature to communicate updates or changes to specific participants.


