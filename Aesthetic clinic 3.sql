CREATE DATABASE  IF NOT EXISTS `hospital` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `hospital`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: hospital
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `administration staff`
--

DROP TABLE IF EXISTS `administration staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administration staff` (
  `Employee_ID` text,
  `Number` int DEFAULT NULL,
  `FName` text,
  `LName` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administration staff`
--

LOCK TABLES `administration staff` WRITE;
/*!40000 ALTER TABLE `administration staff` DISABLE KEYS */;
INSERT INTO `administration staff` VALUES ('Adm1',1,'Cathlene','Callaby'),('Adm2',2,'Doll','Coopper'),('Adm3',3,'Carmela','Sangar'),('Adm4',4,'Pammie','Tolworth');
/*!40000 ALTER TABLE `administration staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `aesthetic clinic`
--

DROP TABLE IF EXISTS `aesthetic clinic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `aesthetic clinic` (
  `Clinic_ID` text,
  `Number` int DEFAULT NULL,
  `Name` text,
  `Location` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aesthetic clinic`
--

LOCK TABLES `aesthetic clinic` WRITE;
/*!40000 ALTER TABLE `aesthetic clinic` DISABLE KEYS */;
INSERT INTO `aesthetic clinic` VALUES ('Cli1',1,'青春之源美容診所','台北市大安區信義路四段123號3樓'),('Cli2',2,'美好時光醫美中心','新北市板橋區中山路456號2樓');
/*!40000 ALTER TABLE `aesthetic clinic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `appointment`
--

DROP TABLE IF EXISTS `appointment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `appointment` (
  `Appointment_ID` text,
  `Number` int DEFAULT NULL,
  `Patient_ID` text,
  `Employee_ID` text,
  `Dia_Ope` text,
  `Time` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointment`
--

LOCK TABLES `appointment` WRITE;
/*!40000 ALTER TABLE `appointment` DISABLE KEYS */;
INSERT INTO `appointment` VALUES ('App1',1,'Pat2','Doc2','Ope1','2024/5/1 9:51'),('App2',2,'Pat10','Doc4','Dia1','2024/5/1 9:56'),('App3',3,'Pat13','Doc1','Dia2','2024/5/1 9:57'),('App4',4,'Pat2','Doc5','Ope2','2024/5/1 9:58'),('App5',5,'Pat12','Doc2','Opp3','2024/5/1 10:58'),('App6',6,'Pat19','Doc2','Dia3','2024/5/1 11:00'),('App7',7,NULL,NULL,'Dia4','2024/06/22 06:05'),('App8',8,'Pat5','Doc1','Ope4','2024/06/20 02:05');
/*!40000 ALTER TABLE `appointment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `buyer`
--

DROP TABLE IF EXISTS `buyer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `buyer` (
  `Employee_ID` text,
  `Number` int DEFAULT NULL,
  `FName` text,
  `LName` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `buyer`
--

LOCK TABLES `buyer` WRITE;
/*!40000 ALTER TABLE `buyer` DISABLE KEYS */;
INSERT INTO `buyer` VALUES ('Buy1',1,'Nikkil','Short'),('Buy2',2,'Stefania','Hamper'),('Buy3',3,'Teador','Scarfe');
/*!40000 ALTER TABLE `buyer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `diagnose`
--

DROP TABLE IF EXISTS `diagnose`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `diagnose` (
  `Diagnose_ID` text,
  `Number` int DEFAULT NULL,
  `Inventory_ID` text,
  `Amount` int DEFAULT NULL,
  `Problem` text,
  `Comment` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `diagnose`
--

LOCK TABLES `diagnose` WRITE;
/*!40000 ALTER TABLE `diagnose` DISABLE KEYS */;
INSERT INTO `diagnose` VALUES ('Dia1',1,'Inv9',1,'皺紋','未來預約注射肉毒桿菌素後解決'),('Dia2',2,'Inv5',1,'雀斑','應該採激光治療或化學換膚等治療方式'),('Dia3',3,'Inv1',1,'痘疤','回去擦藥改善'),('Dia4',4,'TBD',0,NULL,NULL);
/*!40000 ALTER TABLE `diagnose` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctor`
--

DROP TABLE IF EXISTS `doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctor` (
  `Employee_ID` text,
  `Number` int DEFAULT NULL,
  `FName` text,
  `LName` text,
  `License` text,
  `Specialize_in` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor`
--

LOCK TABLES `doctor` WRITE;
/*!40000 ALTER TABLE `doctor` DISABLE KEYS */;
INSERT INTO `doctor` VALUES ('Doc1',1,'Albertine','Scriviner','醫學美容諮詢師','皮膚生理、病理學'),('Doc2',2,'Cybil','Jachimiak','醫學美容師',' 外科整型療程'),('Doc3',3,'Anet','Geeritz','醫學美容師','皮膚美容療程'),('Doc4',4,'Sascha','Napolione','醫學美容護理師',' 光電療程'),('Doc5',5,'Rickie','Huitt','醫學美容諮詢師',' 外科整型療程');
/*!40000 ALTER TABLE `doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory` (
  `Inventory_ID` text,
  `Number` int DEFAULT NULL,
  `Consumables` text,
  `Amount` int DEFAULT NULL,
  `Unit_Price` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES ('Inv1',1,'PVC手套',30,10),('Inv2',2,'果凍凝膠面罩',20,15),('Inv3',3,'生理食鹽水',15,18),('Inv4',4,'紗布',50,22),('Inv5',5,'面膜紙',15,6),('Inv6',6,'酒精棉片',12,11),('Inv7',7,'滾輪針',6,10),('Inv8',8,'肉毒桿菌素',8,15),('Inv9',9,'護膚霜',18,10),('Inv10',10,'面部按摩機',2,15),('Inv11',11,'酒精擦布',25,20),('Inv12',12,'碘酒',10,30),('Inv13',13,'縫合線',40,19),('Inv14',14,'麻醉藥劑',15,28),('Inv15',15,'止血藥劑',4,40),('Inv16',16,'玻尿酸',28,15),('Inv17',17,'聚左旋乳酸',7,13),('Inv18',18,'聚乳酸',18,15),('Inv19',19,'手術刀',10,9);
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `operation`
--

DROP TABLE IF EXISTS `operation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `operation` (
  `Operation_ID` text,
  `Number` int DEFAULT NULL,
  `Tool` text,
  `Inventory_ID` text,
  `Amount` int DEFAULT NULL,
  `Problem` text,
  `Comment` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `operation`
--

LOCK TABLES `operation` WRITE;
/*!40000 ALTER TABLE `operation` DISABLE KEYS */;
INSERT INTO `operation` VALUES ('Ope1',1,'射頻治療儀','Inv19',2,'水腫處理','術後狀況良好'),('Ope2',2,'超聲波治療器材','Inv11',2,'皮膚疼痛治療','無'),('Ope3',3,'波尿酸治療相關器材','Inv16',2,'波尿酸注射','留院觀察'),('Ope4',4,NULL,'TBD',0,NULL,NULL);
/*!40000 ALTER TABLE `operation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient` (
  `Patient_ID` text,
  `Number` int DEFAULT NULL,
  `FName` text,
  `LName` text,
  `Birth_Date` text,
  `Phone_Number` text,
  `Authorize` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient`
--

LOCK TABLES `patient` WRITE;
/*!40000 ALTER TABLE `patient` DISABLE KEYS */;
INSERT INTO `patient` VALUES ('Pat1',1,'Yolane','Foot','07/06/2013','8777197100','TRUE'),('Pat2',2,'Piotr','Peckett','12/20/2013','8229970789','TRUE'),('Pat3',3,'Matty','Andrick','05/15/2012','3958874464','TRUE'),('Pat4',4,'Diann','Lillicrap','03/28/2013','3336926583','FALSE'),('Pat5',5,'Wilden','Pavlenko','12/13/2012','6295202213','TRUE'),('Pat6',6,'Avrit','Baxter','01/01/2010','6008638510','TRUE'),('Pat7',7,'Carolee','Marlowe','07/24/2013','1081099799','FALSE'),('Pat8',8,'Emilia','Posnette','12/17/2014','4176574297','FALSE'),('Pat9',9,'Burtie','Fewster','04/01/2015','9567877899','FALSE'),('Pat10',10,'Merell','Fulton','10/11/2012','3848915604','TRUE'),('Pat11',11,'Maure','Conaghy','12/03/2014','2015911444','FALSE'),('Pat12',12,'Federica','Dugget','03/25/2011','9835375494','TRUE'),('Pat13',13,'Rollin','Sarle','08/18/2013','1072542403','TRUE'),('Pat14',14,'Beulah','Morforth','01/07/2014','6619262525','FALSE'),('Pat15',15,'Tamas','Challen','12/25/2010','3181158922','FALSE'),('Pat16',16,'Birgitta','Meddows','09/19/2010','5412529589','TRUE'),('Pat17',17,'Hinze','Yakutin','04/10/2010','9073129088','FALSE'),('Pat18',18,'Carlota','Ramsden','05/29/2012','8437129796','FALSE'),('Pat19',19,'Yvon','Gomer','11/08/2013','7423298421','TRUE'),('Pat20',20,'Kleon','Maso','10/06/2014','5852029445','FALSE');
/*!40000 ALTER TABLE `patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchaselist`
--

DROP TABLE IF EXISTS `purchaselist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `purchaselist` (
  `Purchaselist_ID` text,
  `Number` int DEFAULT NULL,
  `Employee_ID` text,
  `Inventory_ID` text,
  `Unit_price` int DEFAULT NULL,
  `Amount` int DEFAULT NULL,
  `Total_price` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchaselist`
--

LOCK TABLES `purchaselist` WRITE;
/*!40000 ALTER TABLE `purchaselist` DISABLE KEYS */;
INSERT INTO `purchaselist` VALUES ('Pur1',1,'Buy1','Inv8',20000,3,60000),('Pur2',2,'Buy2','Inv4',5,20,100),('Pur3',3,'Buy3','Inv3',300,10,3000),('Pur4',4,'Buy2','Inv12',250,5,750),('Pur5',5,'Buy1','Inv16',15000,4,60000),('Pur6',6,'Buy1','Inv6',1,100,50),('Pur7',7,'Buy1','Inv11',4,20,80),('Pur8',8,'Buy2','Inv1',2,50,100),('Pur9',9,'Buy2','Inv14',500,10,5000),('Pur10',10,'Buy1','Inv2',450,5,2250);
/*!40000 ALTER TABLE `purchaselist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unit`
--

DROP TABLE IF EXISTS `unit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `unit` (
  `Unit_ID` text,
  `Number` int DEFAULT NULL,
  `Unit_Name` text,
  `Unit_Leader` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unit`
--

LOCK TABLES `unit` WRITE;
/*!40000 ALTER TABLE `unit` DISABLE KEYS */;
INSERT INTO `unit` VALUES ('Uni1',1,'行政管理','Cathlene Callaby'),('Uni2',2,'採購','Teador Scarfe'),('Uni3',3,'醫生','Albertine Scriviner');
/*!40000 ALTER TABLE `unit` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-08  2:08:05
