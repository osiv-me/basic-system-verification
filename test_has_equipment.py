from datachecker import DataChecker

class MockCursor(object):
    def fetchall(self):
        return [(
            340,
            "Kristoffer",
            "Nordstrom",
            39,
            "Male",
            "Ronnvagen 5",
            "37160"
            "Lyckeby",
            "Swedish",
            439,
            101,
            101, 
            "kristoffer.nordstrom@northerntest.se",           
            "SuperSecret",
            ""
        )]

    def fetchall_no_equipment(self):
        return [(
            341,
            "Kristoffer",
            "Nordstrom",
            15,
            "Male",
            "Ronnvagen 5",
            "37160"
            "Lyckeby",
            "Swedish",
            None,
            None,
            None,  
            "kristoffer.nordstrom@northerntest.se",          
            "SuperSecret",
            ""
        )]

    def fetchone(self):
        return (
            101,
           "IMEI_0123456789",
            452,
        )

    def no_return(self):
        return ""

    def execute(self,arg,args):
        return True

class MockConn(object):
    def commit(self):
        return True

class TestClass(object):
    def test_passing(self): 
        self.cursor=MockCursor()
        self.conn=MockConn()
        assert DataChecker.customer_has_equipment_attached(self,340) == True

    def test_no_ptr(self):
        self.cursor=MockCursor()
        self.conn=MockConn()
        self.cursor.fetchall=self.cursor.fetchall_no_equipment
        assert DataChecker.customer_has_equipment_attached(self,340) == False

    def test_empty_equipment(self):
        self.cursor=MockCursor()
        self.conn=MockConn()
        self.cursor.fetchone=self.cursor.no_return
        assert DataChecker.customer_has_equipment_attached(self,340) == False

    def test_id_not_found(self):
        self.cursor=MockCursor()
        self.conn=MockConn()
        self.cursor.fetchall=self.cursor.no_return        
        assert DataChecker.customer_has_equipment_attached(self,340) == False
