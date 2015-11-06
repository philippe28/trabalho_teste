package br.com.tcc.util;

import java.text.ParseException;
import java.util.Date;
import java.util.Map;

import junit.framework.TestCase;

import org.junit.Test;

import br.com.tcc.bo.*;
import br.com.tcc.model.*;


public class Testa extends TestCase{
	
	@Test
	public void testSprintDias() throws ParseException{
		
		Sprint sprint = Main.criaSprint();		
		assertEquals(7, sprint.getQtdeDias());
	}
	
	
	@Test
	public void testSprintHorasTotal() throws ParseException{
		
		Sprint sprint = Main.criaSprint();		
		assertEquals(140.0, sprint.getTotalHoras());
	}
	

	@Test
	public void testDataNula() throws ParseException{
		
		Date date = null;
		assertEquals(null, date);
	}
	
	@SuppressWarnings("deprecation")
	@Test	
	public void testDataInicio() throws ParseException {
		Sprint sprint = Main.criaSprint();
		Date data = new Date(2014,12,01);
		assertEquals(data, sprint.getDtInicio());
		
	
	}	
	
	
	@SuppressWarnings("deprecation")
	@Test
	public void testDataFim() throws ParseException {
		
		Sprint sprint = Main.criaSprint();	
				
		Date data = new Date(2014,12,01);		
				
		assertEquals(data, sprint.getDtFim());
		
	}
	
	@Test
	public void testConsumoDiario() throws ParseException {
		Sprint sprint = Main.criaSprint();
		Map<Date,Double> eixoXY = calculaEixosXYHoras(sprint);
		setTotalHoras(sprint.getTotalHoras());
		
				
		assertEquals(setConsumoDiarioIdeal(5.0/ sprint.getQtdeDias()), sprint);
		
	
	}
	
/*
	@Test
	public void oi() throws ParseException{
		
		ItemHistorico item = (ItemHistorico) Main.criaItensHistorico();
		item.setCodEstoria(2);
		item.setTempoGasto(8);
		item.setData(DataUtil.converteStringParaDate("09/09/2014"));
		Sprint sprint = Main.criaSprint();		
		assertEquals(item,ItemHistorico );
	}
	
*/

	private Map<Date, Double> calculaEixosXYHoras(Sprint sprint) {
		// TODO Auto-generated method stub
		return null;
	}


	private Object setConsumoDiarioIdeal(double d) {
		// TODO Auto-generated method stub
		return null;
	}


	private void setTotalHoras(Double totalHoras) {
		// TODO Auto-generated method stub
		
	}
	
	
}