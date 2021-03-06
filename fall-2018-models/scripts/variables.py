import orca
from urbansim.utils import misc

############################
# small drive network vars #
############################


@orca.column('parcels')
def node_id_small(parcels, netsmall):
    idssmall_parcel = netsmall.get_node_ids(parcels.x, parcels.y)
    return idssmall_parcel


@orca.column('rentals')
def node_id_small(rentals, netsmall):
    idssmall_rentals = netsmall.get_node_ids(
        rentals.longitude, rentals.latitude)
    return idssmall_rentals


@orca.column('buildings')
def node_id_small(parcels, buildings):
    return misc.reindex(parcels.node_id_small, buildings.parcel_id)


@orca.column('units')
def node_id_small(buildings, units):
    return misc.reindex(buildings.node_id_small, units.building_id)


@orca.column('households')
def node_id_small(units, households):
    return misc.reindex(units.node_id_small, households.unit_id)


@orca.column('persons')
def node_id_small(households, persons):
    return misc.reindex(households.node_id_small, persons.household_id)


@orca.column('jobs')
def node_id_small(buildings, jobs):
    return misc.reindex(buildings.node_id_small, jobs.building_id)


###########################
#    walk network vars    #
###########################
@orca.column('parcels')
def node_id_walk(parcels, netwalk):
    idswalk_parcel = netwalk.get_node_ids(parcels.x, parcels.y)
    return idswalk_parcel


@orca.column('rentals')
def node_id_walk(rentals, netwalk):
    idswalk_rentals = netwalk.get_node_ids(rentals.longitude, rentals.latitude)
    return idswalk_rentals


@orca.column('buildings')
def node_id_walk(parcels, buildings):
    return misc.reindex(parcels.node_id_walk, buildings.parcel_id)


@orca.column('units')
def node_id_walk(buildings, units):
    return misc.reindex(buildings.node_id_walk, units.building_id)


@orca.column('households')
def node_id_walk(units, households):
    return misc.reindex(units.node_id_walk, households.unit_id)


@orca.column('persons')
def node_id_walk(households, persons):
    return misc.reindex(households.node_id_walk, persons.household_id)


@orca.column('jobs')
def node_id_walk(buildings, jobs):
    return misc.reindex(buildings.node_id_walk, jobs.building_id)


###########################
#    beam network vars    #
###########################
# @orca.column('parcels')
# def node_id_beam(parcels, netbeam):
#     idsbeam_parcel = netbeam.get_node_ids(parcels.x, parcels.y)
#     return idsbeam_parcel


# @orca.column('rentals')
# def node_id_beam(rentals, netbeam):
#     idsbeam_rentals = netbeam.get_node_ids(
#         rentals.longitude, rentals.latitude)
#     return idsbeam_rentals


# @orca.column('buildings')
# def node_id_beam(parcels, buildings):
#     return misc.reindex(parcels.node_id_beam, buildings.parcel_id)


# @orca.column('jobs')
# def node_id_beam(buildings, jobs):
#     return misc.reindex(buildings.node_id_beam, jobs.building_id)


###############################
#      WLCM dummy columns     #
###############################

@orca.column('jobs')
def sector_retail(jobs):
    return jobs['sector_id'].isin([44, 45]).astype(int)


@orca.column('jobs')
def sector_healthcare(jobs):
    return jobs['sector_id'].isin([62]).astype(int)


@orca.column('jobs')
def sector_tech(jobs):
    return jobs['sector_id'].isin([51, 54]).astype(int)


@orca.column('jobs')
def sector_food_and_hosp(jobs):
    return jobs['sector_id'].isin([72]).astype(int)


@orca.column('jobs')
def sector_mfg(jobs):
    return jobs['sector_id'].isin([31, 32, 33]).astype(int)


@orca.column('jobs')
def sector_edu_serv(jobs):
    return jobs['sector_id'].isin([61]).astype(int)


@orca.column('jobs')
def sector_oth_serv(jobs):
    return jobs['sector_id'].isin([81]).astype(int)


@orca.column('jobs')
def sector_constr(jobs):
    return jobs['sector_id'].isin([23]).astype(int)


@orca.column('jobs')
def sector_gov(jobs):
    return jobs['sector_id'].isin([92]).astype(int)


@orca.column('jobs')
def sector_fire(jobs):
    return jobs['sector_id'].isin([52, 53]).astype(int)


@orca.column('jobs')
def sector_whlsale(jobs):
    return jobs['sector_id'].isin([42]).astype(int)


@orca.column('jobs')
def sector_admin(jobs):
    return jobs['sector_id'].isin([56]).astype(int)


@orca.column('jobs')
def sector_transport(jobs):
    return jobs['sector_id'].isin([48]).astype(int)


@orca.column('jobs')
def sector_arts(jobs):
    return jobs['sector_id'].isin([71]).astype(int)


@orca.column('jobs')
def sector_util(jobs):
    return jobs['sector_id'].isin([22]).astype(int)


@orca.column('jobs')
def parcel_id(jobs, buildings):
    return misc.reindex(
        buildings.parcel_id, jobs.building_id)


@orca.column('persons')
def no_higher_ed(persons):
    return (persons['edu'] < 21).astype(int)


@orca.column('persons')
def age_under_45(persons):
    return (persons['age'] < 45).astype(int)


@orca.column('households')
def hh_inc_under_25k(households):
    return ((
        households['income'] < 25000) & (
        households['income'] > 10)).astype(int)


@orca.column('households')
def hh_inc_25_to_75k(households):
    return ((
        households['income'] >= 25000) & (
        households['persons'] < 75000)).astype(int)


@orca.column('households')
def hh_inc_75_to_200k(households):
    return ((
        households['income'] >= 75000) & (
        households['income'] < 200000)).astype(int)


# cols for WLCM interaction terms
@orca.column('jobs')
def zone_id_work(jobs, parcels):
    return misc.reindex(
        parcels.zone_id, jobs.parcel_id)


@orca.column('persons')
def zone_id_home(persons, households, units, buildings, parcels):
    return misc.reindex(
        orca.merge_tables(
            households, [households, units, buildings, parcels],
            columns=['zone_id'])['zone_id'],
        persons.household_id).astype(float)
