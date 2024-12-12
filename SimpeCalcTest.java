import org.junit.jupiter.api.Test;
import  static org.junit.jupiter.api.Assertions.*;

import java.beans.Transient;
class SimpleCalcTest{

    @Transient
    void twoTwo(){
        var calculator = new SimpleCalc();
        assertEquals(4, calculator.add(2,2));

    }
}