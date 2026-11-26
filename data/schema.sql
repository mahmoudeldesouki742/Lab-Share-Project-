CREATE TABLE IF NOT EXISTS  Users (
    user_id INTEGER PRIMARY KEY  AUTOINCREMENT ,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    full_name TEXT NOT NULL ,
    role TEXT NOT NULL CHECK(role IN( 'Admin' ,'Researcher')),
    created_at TEXT DEFAULT CURRENT_TIMESTAMP

);

CREATE TABLE IF NOT EXISTS Categories(
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE ,
    description TEXT
);

CREATE TABLE IF NOT EXISTS Equipment(
    equipment_id INTEGER  PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL  ,
    category_id INTEGER NOT NULL ,
    serial_number TEXT UNIQUE,
    location TEXT,
    description TEXT ,
    status TEXT NOT NULL DEFAULT 'Available'
    CHECK (status IN ('Available', 'Under Maintenance', 'Retired')),
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS Reservations(
    reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL, 
    equipment_id INTEGER NOT NULL ,
    start_time TEXT NOT NULL,
    end_time TEXT NOT NULL,
    purpose TEXT ,
    status TEXT NOT NULL DEFAULT 'Pending' CHECK (status IN ('Pending','Approved','Rejected','Cancelled','Completed')),
    rejection_reason TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES Users(user_id) ON DELETE RESTRICT,
    FOREIGN KEY (equipment_id) REFERENCES Equipment(equipment_id) ON DELETE RESTRICT,
    CHECK (end_time > start_time)


);

CREATE TABLE IF NOT EXISTS Maintenance(
    maintenance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    equipment_id INTEGER NOT NULL ,
    reported_by INTEGER NOT NULL  ,
    description TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'Open' CHECK(status IN ('Open','In Progress','Completed')),
    reported_at TEXT DEFAULT CURRENT_TIMESTAMP,
    completed_at TEXT,
    FOREIGN KEY(equipment_id) REFERENCES Equipment(equipment_id) ON DELETE RESTRICT ,
    FOREIGN KEY (reported_by) REFERENCES Users(user_id) ON DELETE RESTRICT


);

CREATE TABLE IF NOT EXISTS Reservation_History(
    history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    reservation_id INTEGER NOT NULL ,
    old_status TEXT,
    new_status TEXT NOT NULL,
    changed_by INTEGER NOT NULL ,
    changed_at TEXT DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    FOREIGN KEY(reservation_id) REFERENCES Reservations(reservation_id) ON DELETE RESTRICT,
    FOREIGN KEY(changed_by) REFERENCES Users(user_id) ON DELETE RESTRICT

);
