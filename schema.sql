DROP TABLE IF EXISTS "properties";
DROP TABLE IF EXISTS "provinces";

CREATE TABLE "properties" (
	"id" INTEGER PRIMARY KEY AUTOINCREMENT,
	"x" INTEGER,
	"y" INTEGER,
	"title" TEXT,
	"price" REAL,
	"description" TEXT,
	"beds" INTEGER,
	"baths" INTEGER,
	"squareMeters" INTEGER
);

CREATE TABLE "provinces" (
	"name" TEXT,
	"upperLeftX" INTEGER,
	"upperLeftY" INTEGER,
	"bottomRightX" INTEGER,
	"bottomRightY" INTEGER
);