# Sovelluksen tietokanta


## Tietokantakaavio

![alt text](https://github.com/ansolotli/Tutkimussovellus/blob/master/documentation/pics/tsoha_database.jpg)

## CREATE TABLE -lauseet

```
CREATE TABLE site (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(144) NOT NULL,
        PRIMARY KEY (id)
)
```

```
CREATE TABLE account (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(144) NOT NULL,
        username VARCHAR(144) NOT NULL,
        password VARCHAR(144) NOT NULL,
        PRIMARY KEY (id)
)
```

```
CREATE TABLE sample (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        samplename VARCHAR(144) NOT NULL,
        sampletype VARCHAR(144) NOT NULL,
        species VARCHAR(144) NOT NULL,
        amount VARCHAR(144) NOT NULL,
        site_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(site_id) REFERENCES site (id)
)
```

```
CREATE TABLE users_sites (
        site_id INTEGER,
        user_id INTEGER,
        FOREIGN KEY(site_id) REFERENCES site (id),
        FOREIGN KEY(user_id) REFERENCES account (id)
)
```

```
CREATE TABLE users_samples (
        sample_id INTEGER,
        user_id INTEGER,
        FOREIGN KEY(sample_id) REFERENCES sample (id),
        FOREIGN KEY(user_id) REFERENCES account (id)
)
```