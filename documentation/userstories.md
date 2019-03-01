### User stories

Kirjautumattomana käyttäjänä haluan | SQL-lause toteutetulle toiminnallisuudelle
--- | ---
luoda uuden käyttäjätunnuksen | INSERT INTO account (date_created, date_modified, name, username, password) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)
kirjautua sisään | SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS account_date_modified, account.name AS account_name, account.username AS account_username, account.password AS account_password FROM account WHERE account.username = ? AND account.password = ?
nähdä sovellukseen tallennetut tutkimuspaikat | SELECT site.id AS site_id, site.date_created AS site_date_created, site.date_modified AS site_date_modified, site.name AS site_name FROM site ORDER BY site.name
nähdä kustakin tutkimuspaikasta otetut näytteet |  SELECT sample.id AS sample_id, sample.date_created AS sample_date_created, sample.date_modified AS sample_date_modified, sample.samplename AS sample_samplename, sample.sampletype AS sample_sampletype, sample.species AS sample_species, sample.amount AS sample_amount, sample.site_id AS sample_site_id FROM sample WHERE ? = sample.site_id
hakea sovelluksesta tutkimuspaikkoja paikannimen perusteella | SELECT site.id AS site_id, site.date_created AS site_date_created, site.date_modified AS site_date_modified, site.name AS site_name FROM site WHERE site.name LIKE ?
hakea sovelluksesta näytteitä tyypin (esim. pohjaeläinnäyte) perusteella |
hakea sovelluksesta näytteitä näytteenottoajankohdan perusteella |
hakea sovelluksesta näytteitä siinä esiintyvän lajin perusteella |

Kirjautuneena käyttäjänä haluan | SQL-lause toteutetulle toiminnallisuudelle
--- | ---
lisätä sovellukseen uuden tutkimuspaikan |  INSERT INTO site (date_created, date_modified, name) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?)
muokata olemassaolevia tutkimuspaikkoja | UPDATE site SET date_modified=CURRENT_TIMESTAMP, name=? WHERE site.id = ?
poistaa olemassaolevia tutkimuspaikkoja | DELETE FROM site WHERE site.id = ?
lisätä tiettyyn tutkimuspaikkaan liittyvän näytteen |  INSERT INTO sample (date_created, date_modified, samplename, sampletype, species, amount, site_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?)
muokata näytteitä | UPDATE sample SET date_modified=CURRENT_TIMESTAMP, samplename=?, sampletype=?, species=?, amount=? WHERE sample.id = ?
poistaa näytteitä | DELETE FROM sample WHERE sample.id = ?
nähdä, montako tutkimuspaikkaa olen lisännyt sovellukseen | SELECT COUNT(users_sites.site_id) FROM users_sites WHERE user_id = ?
nähdä, montako näytettä olen lisännyt sovellukseen | SELECT COUNT(users_samples.sample_id) FROM users_samples WHERE user_id = ?
tarkastella tutkimuspaikkoja, jotka olen itse tallentanut sovellukseen | SELECT site.name AS name FROM site LEFT JOIN users_sites ON site.id = users_sites.site_id WHERE users_sites.user_id = ?
tarkastella näytteitä, jotka olen itse tallentanut sovellukseen | SELECT site.id as siteid, site.name as sitename, sample.samplename as samplename, sample.id as sampleid FROM users_samples JOIN sample ON sample.id = users_samples.sample_id JOIN site ON site.id = sample.site_id WHERE users_samples.user_id = ? ORDER BY site.name
nähdä, montako näytettä kullakin tutkimuspaikalla on |  SELECT site.name AS name, COUNT(sample.id) AS count FROM sample LEFT JOIN site ON site.id = sample.site_id GROUP BY name ORDER BY count DESC
nähdä, montako näytettä kutakin näytetyyppiä on | SELECT sample.sampletype AS type, COUNT(sample.id) AS count FROM sample GROUP BY type ORDER BY count DESC
nähdä, montako näytettä kutakin näytetyyppiä kullakin tutkimuspaikalla on | SELECT site.name AS name, sample.sampletype AS type, COUNT(sample.id) AS count FROM sample LEFT JOIN site ON site.id = sample.site_id GROUP BY name, type ORDER BY count DESC
nähdä, monessako näytteessä kukin laji esiintyy | SELECT sample.species AS species, COUNT(sample.id) AS count FROM sample GROUP BY species ORDER BY count DESC
nähdä, monessako näytteessä kukin laji esiintyy kullakin tutkimuspaikalla | SELECT site.name AS name, sample.species AS species, COUNT(sample.id) AS count FROM sample LEFT JOIN site ON site.id = sample.site_id GROUP BY name, species ORDER BY count DESC
nähdä, monellako käyttäjällä on näytteitä kullakin tutkimuspaikalla | SELECT site.name AS site, COUNT(DISTINCT account.id) AS count FROM account LEFT JOIN users_samples ON users_samples.user_id = account.id LEFT JOIN sample ON sample.id = users_samples.sample_id LEFT JOIN site ON site.id = sample.site_id GROUP BY site.id ORDER BY count DESC, site
