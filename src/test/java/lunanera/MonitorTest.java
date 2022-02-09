package lunanera;

import com.intelligt.modbus.jlibmodbus.Modbus;
import com.intelligt.modbus.jlibmodbus.data.ModbusHoldingRegisters;
import com.intelligt.modbus.jlibmodbus.exception.ModbusIOException;
import com.intelligt.modbus.jlibmodbus.exception.ModbusNumberException;
import com.intelligt.modbus.jlibmodbus.exception.ModbusProtocolException;
import com.intelligt.modbus.jlibmodbus.master.ModbusMaster;
import com.intelligt.modbus.jlibmodbus.master.ModbusMasterFactory;
import com.intelligt.modbus.jlibmodbus.msg.request.ReadHoldingRegistersRequest;
import com.intelligt.modbus.jlibmodbus.msg.response.ReadHoldingRegistersResponse;
import com.intelligt.modbus.jlibmodbus.serial.SerialParameters;
import com.intelligt.modbus.jlibmodbus.serial.SerialPort;
import com.intelligt.modbus.jlibmodbus.serial.SerialPortFactoryPJC;
import com.intelligt.modbus.jlibmodbus.serial.SerialUtils;
import org.junit.jupiter.api.Test;

import java.math.BigDecimal;
import java.math.RoundingMode;

class MonitorTest {

    @Test
    void testConnection() throws Exception {
        SerialParameters sp = new SerialParameters();
        Modbus.setLogLevel(Modbus.LogLevel.LEVEL_WARNINGS);

        sp.setDevice("COM4");

        sp.setBaudRate(SerialPort.BaudRate.BAUD_RATE_19200);
        sp.setDataBits(8);
        sp.setParity(SerialPort.Parity.NONE);
        sp.setStopBits(1);

        SerialPortFactoryPJC factory = new SerialPortFactoryPJC();
        System.out.println(factory.getPortIdentifiersImpl());
        System.out.println(factory.available());

        SerialUtils.setSerialPortFactory(factory)

        ModbusMaster m = ModbusMasterFactory.createModbusMasterRTU(sp);
        m.setResponseTimeout(500);
        m.connect();

        System.out.println(m.isConnected());

        read(5, m);

        read(3, m);

        read(5, m);

    }

    private void read(final int  slaveId, final ModbusMaster m) throws ModbusNumberException, ModbusProtocolException, ModbusIOException {
        ReadHoldingRegistersRequest request = new ReadHoldingRegistersRequest();
        request.setServerAddress(slaveId);
        request.setStartAddress(0);
        request.setQuantity(1);
        ReadHoldingRegistersResponse response = (ReadHoldingRegistersResponse) request.getResponse();

        m.processRequest(request);
        ModbusHoldingRegisters registers = response.getHoldingRegisters();
        for (int r : registers) {
            BigDecimal pv =  BigDecimal.valueOf(r).divide(BigDecimal.valueOf(10), 1, RoundingMode.UNNECESSARY);
            System.out.println("Slave " + slaveId + " pv="  + pv);
        }
    }
}