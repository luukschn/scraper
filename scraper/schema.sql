DROP TABLE IF EXISTS huurwoningen;

--find out correct structure and data stuff
--why use nvarchar over TEXT? which is better?
CREATE TABLE woningen (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    prijs NVARCHAR NOT NULL,
    grootte NVARCHAR NOT NULL,
    kamers NVARCHAR NOT NULL,
    locatie NVARCHAR,
    wijk NVARCHAR NOT NULL,
    link NVARCHAR NOT NULL,
    source NVARCHAR,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);