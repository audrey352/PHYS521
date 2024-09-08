from astropy import units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

def plot_vis(coordinates):
    # Montreal location and times
    mtl = EarthLocation(lat=45.5019*u.deg, lon=-73.5674*u.deg, height=45*u.m) # approximatingf average altitude as 45m
    times_sept13 = '2024-09-13 '+np.array(['19','20','21', '22', '23'])+':00:00'
    times_sept14 = '2024-09-14 '+np.array(['00', '01', '02', '03', '04', '05', '06'])+':00:00'
    obs_time = Time((np.concatenate((times_sept13,times_sept14))))
    
    # Convert object coordinates to mtl frame
    altaz_frame = AltAz(obstime=obs_time, location=mtl)
    coords_altaz = coordinates.transform_to(altaz_frame)  # get alt & az of M33 at given times

    # Plot
    plt.figure(figsize=(8, 6))
    plt.scatter(obs_time.datetime, coords_altaz.alt.deg, color='k')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H'))
    plt.xticks(rotation=90)
    plt.title(f"Visibility of M33 (ra = {coordinates.ra.deg}, dec = {coordinates.dec.deg})\nfrom Montreal, 2024-09-13")
    plt.xlabel("Time [UCT]")
    plt.ylabel("Altitude [deg]")
    plt.tight_layout()
    plt.savefig("visibility_plot.pdf")
    plt.show()

# values from https://simbad.u-strasbg.fr/simbad/sim-id?Ident=M33
M33_coord = SkyCoord('01 33 50.8965749232 +30 39 36.630403128', unit=(u.hourangle, u.deg))
plot_vis(M33_coord)