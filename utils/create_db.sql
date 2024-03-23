create database p1meter;
create table test
(
    id        serial,
    "1.8.1"   double precision,
    "1.8.2"   double precision,
    "2.8.1"   double precision,
    "2.8.2"   double precision,
    "96.14.0" double precision,
    "1.7.0"   double precision,
    "2.7.0"   double precision,
    "17.0.0"  double precision,
    "96.3.10" double precision,
    "96.7.21" double precision,
    "96.7.9"  double precision,
    "32.32.0" double precision,
    "52.32.0" double precision,
    "72.32.0" double precision,
    "32.36.0" double precision,
    "52.36.0" double precision,
    "72.36.0" double precision,
    "31.7.0"  double precision,
    "51.7.0"  double precision,
    "71.7.0"  double precision,
    "21.7.0"  double precision,
    "41.7.0"  double precision,
    "61.7.0"  double precision,
    "22.7.0"  double precision,
    "42.7.0"  double precision,
    "62.7.0"  double precision,
    "24.2.1"  double precision,
    "24.3.0"  double precision,
    "timestamp" timestamp
);

comment on column p1data."1.8.1" is 'Meter Reading electricity delivered to client (Tariff 1) in kWh';
comment on column p1data."1.8.2" is 'Meter Reading electricity delivered to client (Tariff 2) in kWh';
comment on column p1data."2.8.1" is 'Meter Reading electricity delivered by client (Tariff 1) in kWh';
comment on column p1data."2.8.2" is 'Meter Reading electricity delivered by client (Tariff 2) in kWh';
comment on column p1data."96.14.0" is 'Tariff indicator electricity';
comment on column p1data."1.7.0" is 'Actual electricity power delivered (+P) in kW';
comment on column p1data."2.7.0" is 'Actual electricity power received (-P) in kW';
comment on column p1data."17.0.0" is 'The actual threshold electricity in kW';
comment on column p1data."96.3.10" is 'Switch position electricity';
comment on column p1data."96.7.21" is 'Number of power failures in any phase';
comment on column p1data."96.7.9" is 'Number of long power failures in any phase';
comment on column p1data."32.32.0" is 'Number of voltage sags in phase L1';
comment on column p1data."52.32.0" is 'Number of voltage sags in phase L2';
comment on column p1data."72.32.0" is 'Number of voltage sags in phase L3';
comment on column p1data."32.36.0" is 'Number of voltage swells in phase L1';
comment on column p1data."52.36.0" is 'Number of voltage swells in phase L2';
comment on column p1data."72.36.0" is 'Number of voltage swells in phase L3';
comment on column p1data."31.7.0" is 'Instantaneous current L1 in A';
comment on column p1data."51.7.0" is 'Instantaneous current L2 in A';
comment on column p1data."71.7.0" is 'Instantaneous current L3 in A';
comment on column p1data."21.7.0" is 'Instantaneous active power L1 (+P) in kW';
comment on column p1data."41.7.0" is 'Instantaneous active power L2 (+P) in kW';
comment on column p1data."61.7.0" is 'Instantaneous active power L3 (+P) in kW';
comment on column p1data."22.7.0" is 'Instantaneous active power L1 (-P) in kW';
comment on column p1data."42.7.0" is 'Instantaneous active power L2 (-P) in kW';
comment on column p1data."62.7.0" is 'Instantaneous active power L3 (-P) in kW';
comment on column p1data."24.2.1" is 'Last hourly value (temperature converted), gas delivered to client in m3';
comment on column p1data."timestamp" is 'Timestamp of measurement as ''YYYY-MM-DD HH:MM:SS''';