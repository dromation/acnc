BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "ACNC_MACHINEINFO" (
	"idnum"	INTEGER
	"machinename"	TEXT
	"manufacturername"	TEXT
	"machinefirstdate" NUMERIC
	"machinetype"	TEXT
	"machineclass"	TEXT
	"machineserialnum" TEXT
	"machinefirstdate" NUMERIC
	"machinehours"	NUMERIC
	"machineoveralparts" NUMERIC
	

);

CREATE TABLE IF NOT EXISTS "ACNC_INPUT" (
	"id_date"	INTEGER
);
CREATE TABLE IF NOT EXISTS "ACNC_OUTPUT" (
	"id_date"	INTEGER
);
CREATE TABLE IF NOT EXISTS "ACNC_5MS" (
	"MAN"	INTEGER,
	"METHOD"	INTEGER,
	"MEASURMENT"	INTEGER,
	"MATERIAL"	INTEGER,
	"MACHINE"	INTEGER
);
CREATE TABLE IF NOT EXISTS "ACNC_SYSTEM" (
	"5M"	INTEGER,
	"FUNCTION"	INTEGER,
	"PART"	INTEGER,
	"STATUS"	INTEGER
);
CREATE TABLE IF NOT EXISTS "ACNC_PARTS" (
	"PART_NAME"	INTEGER,
	"PART_NUMBER"	INTEGER,
	"PART_IMDS"	INTEGER,
	"PART_REF"	INTEGER,
	"PART_TYPE"	INTEGER
);
CREATE TABLE IF NOT EXISTS "ACNC_STATUS" (
	"NEW"	INTEGER,
	"INWORK"	INTEGER,
	"INREVIEW"	INTEGER,
	"INTEST"	INTEGER,
	"OBSOLETE"	INTEGER,
	"REUSED"	INTEGER,
	"REWORK"	INTEGER,
	"DESTROYED"	TEXT,
	"STORED"	INTEGER,
	"SCRAPED"	INTEGER
);
CREATE TABLE IF NOT EXISTS "ACNC_MFMA" (
	"PART_NAME"	INTEGER,
	"SISTEM_TYPE"	INTEGER,
	"FUNCTION"	INTEGER,
	"FAILURE_MODE"	TEXT,
	"FM_NUMBER"	NUMERIC,
	"EFFECT"	TEXT,
	"EF_NUMBER"	NUMERIC,
	"CAUSE"	TEXT,
	"C_NUMBER"	NUMERIC
);
CREATE TABLE IF NOT EXISTS "ACNC_FUNCTIONS" (
	"ELECTRICAL"	INTEGER,
	"OPTICAL"	INTEGER,
	"MECHANICAL"	INTEGER,
	"LEGAL"	INTEGER,
	"SAFETY"	INTEGER,
	"PROCESS"	INTEGER
);
CREATE TABLE IF NOT EXISTS "ACNC_TYPES" (
	"TEMP_VALUE"	INTEGER,
	"CONNECTION"	NUMERIC,
	"BRIDGE"	NUMERIC,
	"LOGICAL"	NUMERIC,
	"CONTROLER"	INTEGER,
	"COMPILER"	INTEGER,
	"LOOP"	INTEGER,
	"RESISTOR"	INTEGER,
	"TRANSISTOR"	INTEGER,
	"SAFETY"	INTEGER,
	"EMERGENCY"	INTEGER,
	"POWER_ON"	INTEGER,
	"POWER_OFF"	INTEGER,
	"POWER_SUPPLY"	INTEGER,
	"ENGINE"	INTEGER,
	"MOTOR_ON"	INTEGER,
	"MOTOR_OFF"	INTEGER,
	"MOTOR_RUN"	INTEGER,
	"START"	INTEGER,
	"STOP"	INTEGER,
	"FOWARD"	INTEGER,
	"REVERSE"	INTEGER,
	"HOLD"	INTEGER,
	"TRUE"	INTEGER,
	"FALSE"	INTEGER,
	"RESTART"	INTEGER,
	"PROGRAM"	INTEGER,
	"CODE"	INTEGER,
	"SYNTHAX"	INTEGER,
	"ERROR"	INTEGER,
	"REPORT"	INTEGER,
	"MONITOR"	INTEGER,
	"WRITE"	INTEGER,
	"READ"	INTEGER,
	"SAVE"	INTEGER,
	"DELETE"	INTEGER,
	"SUPPLY"	INTEGER,
	"CALCULATE"	INTEGER,
	"PROCESSOR"	INTEGER,
	"PROCESS"	INTEGER,
	"SEND"	INTEGER,
	"WIRE"	INTEGER,
	"WIRE_SUPPLY"	INTEGER,
	"WIRE_BRIDGE"	INTEGER,
	"WIRE_CONNECT"	INTEGER,
	"BRAKE"	INTEGER,
	"PAUSE"	INTEGER,
	"MACHINE"	INTEGER,
	"TURNNING"	INTEGER,
	"ROTATE"	INTEGER,
	"TOOL"	INTEGER,
	"TOOL_CHANGE"	INTEGER,
	"TOOL_ERROR"	INTEGER,
	"TOOL_STOP"	INTEGER,
	"TOOL_START"	INTEGER,
	"TOOL_END"	INTEGER,
	"M_START"	INTEGER,
	"M_END"	INTEGER,
	"M_DATA"	INTEGER,
	"M_DATE"	INTEGER,
	"M_PROGRAM"	INTEGER,
	"M_CODE"	INTEGER,
	"G_START"	INTEGER,
	"G_END"	INTEGER,
	"T_CHANGE"	INTEGER,
	"TOOL_SELECT"	INTEGER,
	"TOOL_EJECT"	INTEGER,
	"SETTING_SAVE"	INTEGER,
	"CODE_SAVE"	INTEGER,
	"RS232_ERROR"	INTEGER,
	"CONNECTOR_ERROR"	INTEGER,
	"SIGNAL_ERROR"	INTEGER,
	"SIGNAL_LOW"	INTEGER,
	"SIGNAL_OVERFLOW"	INTEGER,
	"OVERCURRENT"	INTEGER,
	"LOWSUPPLY"	INTEGER,
	"LOWVOLTAGE"	INTEGER,
	"FREQUENCY"	INTEGER,
	"DEFLECT"	INTEGER,
	"REFLECT"	INTEGER,
	"JOINT"	INTEGER,
	"HOLD_POSITION"	INTEGER,
	"JOINT_MOVE"	INTEGER,
	"JOINT_ROTATE"	INTEGER,
	"JOINT_ERROR"	INTEGER,
	"SIGNAL_LOST"	INTEGER,
	"DEBUG"	INTEGER,
	"DEBUG_ERROR"	INTEGER,
	"DEBUG_LOOP"	INTEGER,
	"OVERPRESSURE"	INTEGER,
	"PRESSURE"	INTEGER,
	"UNDERPRESSSURE"	INTEGER,
	"TEMEPRATURE"	INTEGER,
	"TEMP_HOLD"	INTEGER,
	"TEMP_LOW"	INTEGER,
	"TEMP_HIGH"	INTEGER,
	"TEMP_FREQ"	INTEGER,
	"VOLT_LOW"	INTEGER,
	"VOLT_HIGH"	INTEGER,
	"VOLT_FREQ"	INTEGER,
	"VOLT_VALUE"	INTEGER,
	"JOB_START"	INTEGER,
	"JOB_END"	INTEGER,
	"JOB_MOD"	INTEGER,
	"JOB_SELECT"	INTEGER,
	"JOB_RUN"	INTEGER,
	"JOB_STOP"	INTEGER,
	"POTENCIOMETER"	INTEGER,
	"POTEN_ON"	INTEGER,
	"POTEN_FREQ"	INTEGER,
	"POTEN_OFF"	INTEGER,
	"POTEN_ERROR"	INTEGER,
	"AC_POWER"	INTEGER,
	"DC_POWER"	INTEGER,
	"AC_START"	INTEGER,
	"AC_STOP"	INTEGER,
	"DC_START"	INTEGER,
	"DC_STOP"	INTEGER
);
CREATE TABLE IF NOT EXISTS "ACNC_FAILURES" (
	"ID_FAILURE"	INTEGER,
	"WHERE_TYPE"	INTEGER,
	"FAILURE_NUMBER"	INTEGER,
	"WHERE_FUNCTION"	INTEGER
);
CREATE TABLE IF NOT EXISTS "ACNC_CAUSES" (
	"ID_CAUSE"	INTEGER,
	"WHERE_TYPE"	INTEGER,
	"CAUSE_NUMBER"	INTEGER,
	"WHERE_FUNCTION"	INTEGER
);
CREATE TABLE IF NOT EXISTS "ACNC_EFFECTS" (
	"ID_EFFECT"	INTEGER,
	"WHERE_TYPE"	INTEGER,
	"EFFECT_NUMBER"	INTEGER,
	"WHERE_FUNCTION"	INTEGER
);
INSERT INTO "ACNC_TYPES" VALUES (NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "ACNC_TYPES" VALUES (NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "ACNC_TYPES" VALUES (NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "ACNC_TYPES" VALUES (NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "ACNC_TYPES" VALUES (NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "ACNC_TYPES" VALUES (NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
COMMIT;
