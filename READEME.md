sklearn
-------
Topic mining and document clustering proof of concept.

afloat.mishapData is split 80/20 train/test with files separated by category. This is based on RPRT_CATG_C for aviation reports and MISHAP_CLASSN_C for consolidated reports.
Each report is filed in a separate text file named <HTID>.txt

Directory structure:
	+------ test
	|	+------ afloat.mishap
	|	+------ cn.hazard
	|	+------ diving
	|	+------ diving.mishap
	|	+------ hazard.atc
	|	+------ hazard.bash
	|	+------ hazard.embarked.landing
	|	+------ hazard.general
	|	+------ hazard.nma
	|	+------ hazard.phys.episode
	|	+------ mishap
	|	+------ motorcycle
	|	+------ mv.mishap
	|	+------ mv.on.duty
	|	+------ off.duty.rec
	|	+------ pedestrian.bicyclist
	|	+------ pmv.gmv
	|	+------ pt
	|	+------ ship
	|	+------ shore.ground
	|	+------ sub
	+------ train
		+------ afloat.mishap
		+------ cn.hazard
		+------ diving
		+------ hazard.atc
		+------ hazard.bash
		+------ hazard.embarked.landing
		+------ hazard.general
		+------ hazard.nma
		+------ hazard.phys.episode
		+------ mishap
		+------ motorcycle
		+------ mv.mishap
		+------ mv.on.duty
		+------ off.duty.rec
		+------ pedestrian.bicyclist
		+------ pmv.gmv
		+------ pt
		+------ ship
		+------ shore.ground
		+------ shore.mishap
		+------ sub

Format of each file:

docId: <htId>
subj:  <Event short narrative>
EVENT_NARR: <Event full narrative>
AMED_ANALS_NARR: <Aviation only. Aeromedical analysis narrative if present>
DMG_CMTS: <Aviation only. Damage comments if present>
EGR_SRVEL_RSQ_CMTS: <Aviation only. Egress/Surrvival/rescue comments if present>
HF_ACRW_PRFL_CMTS: <Aviation only. Human factor comments if present>
HFACS_EVENT_CMTS: <Aviation only. Human factor event comments if present>
INJ_CMTS: <Aviation only. Injury comments if present>
INVLVD_FAC_NARR: <Aviation only. Involved factor comments if present>
PRIV_MISHAP_ANALYSIS_NARR: <Aviation only. Priv. mishap analysis narrative if present>

