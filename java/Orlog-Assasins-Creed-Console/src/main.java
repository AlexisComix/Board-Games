import java.util.Arrays;
import java.util.Scanner;

public class main {
	static Scanner in = new Scanner(System.in);
	static player player1;
	static player player2;
	static player turn;
	public static boolean checkName(String name) {
		return name.indexOf(" ") == -1 && name.indexOf("-")==-1;
	}
	public static void print(Object o) {
		System.out.print(o);
	}
	public static void println(Object o) {
		System.out.println(o);
	}
	
	public static String input(String str) {
		print(str);
		String intake = in.nextLine();
		return intake;
	}
	
	public static void executeCommand(String command, String Arguments) {
		if(command.equals("Orlog")) {
			TakeNames(Arguments);
		}else if(command.equals("roll")) {
			if(TakeRolls(Arguments)) {
				println("OK");
			}
		}else if(command.equals("godfavor")) {
			if(TakeGodFavor(Arguments)) {
				println("OK");
			}
		}else {
			println("Kindly enter correct command...");
		}
	}
	public static void executeCommand(String command) {
		if(command.equals("print")) {
			printPlayers();
		}else if(command.equals("turn")) {
			if(turn.equals(player1)) {
				println(player2.getName());
				turn = player2;
			}else {
				println(player1.getName());
				turn = player1;
			}
		}else if(command.equals("evaluate")) {
			if(player1.getRolls()==null||player2.getRolls()==null) {
				println("Play rolls first...");
			}else {
				Evaluate();
			}
		}else {
			println("Kindly enter correct command...");
		}
	}
	
	public static void Evaluate() {
		player1.UseRoll();
		player2.UseRoll();
		int player1Melee = player1.getMeleeAttack()-player2.getMeleeDefense();
		int player2Melee = player2.getMeleeAttack()-player1.getMeleeDefense();
		int player1Range = player1.getRangeAttack()-player2.getRangeDefense();
		int player2Range = player2.getRangeAttack()-player1.getRangeDefense();
		if(player1Melee>0) {
			player2.setLifePoints(player2.getLifePoints()-player1Melee);
		}if(player1Range>0) {
			player2.setLifePoints(player2.getLifePoints()-player1Range);
		}if(player2Melee>0) {
			player1.setLifePoints(player1.getLifePoints()-player2Melee);
		}if(player2Range>0) {
			player1.setLifePoints(player1.getLifePoints()-player2Range);
		}if(player2.getGodPower()>0) {
			int difference = player2.getGodPower()-player1.getSteal();
			if(difference<0) {
				player1.setSteal(player1.getSteal()+difference);
			}
			player2.setGodPower(player2.getGodPower()-player1.getSteal());
			player1.setGodPower(player1.getGodPower()+player1.getSteal());
		}if(player1.getGodPower()>0) {
			int difference = player1.getGodPower()-player2.getSteal();
			if(difference<0) {
				player2.setSteal(player2.getSteal()+difference);
			}
			player1.setGodPower(player1.getGodPower()-player2.getSteal());
			player2.setGodPower(player2.getGodPower()+player2.getSteal());
		}GodFavorEvaluate();
		if(player1.getLifePoints()<1) {
			if(player2.getLifePoints()<1) {
				println("Draw");
			}else {
				println(player2.getName()+" wins");
			}
		}else if(player2.getLifePoints()<1) {
			println(player1.getName()+" wins");
		}else {
			printPlayers();
		}resetPlayers();
	}
	
	public static void GodFavorEvaluate() {
		try {
			godFavor player1GodFavor = new godFavor(player1.getGodFavorSelected(), player1.getGodFavorLevel());
			godFavor player2GodFavor = new godFavor(player2.getGodFavorSelected(), player2.getGodFavorLevel());
			if(player1GodFavor.getCost()<player1.getGodPower()) {				
				if(player1GodFavor.getName().equals("TT")) {
					player2GodFavor = new godFavor(player2.getGodFavorSelected(), player2.getGodFavorLevel()-player1GodFavor.getEffect());
				}
			}else if(player2GodFavor.getCost()<player1.getGodPower()) {				
				if(player2GodFavor.getName().equals("TT")) {
					player1GodFavor = new godFavor(player1.getGodFavorSelected(), player1.getGodFavorLevel()-player2GodFavor.getEffect());
				}
			}if(player1GodFavor.getCost()<player1.getGodPower()) {
				if(player1GodFavor.getName().equals("TS")) {
					player2.setLifePoints(player2.getLifePoints()-player1GodFavor.getEffect());
				}else if(player1GodFavor.getName().equals("IR")){
					player1.setLifePoints(player1.getLifePoints()+player1GodFavor.getEffect());
				}
			}if(player2GodFavor.getCost()<player2.getGodPower()) {
				if(player2GodFavor.getName().equals("TS")) {
					player1.setLifePoints(player1.getLifePoints()-player2GodFavor.getEffect());
				}else if(player2GodFavor.getName().equals("IR")) {
					player2.setLifePoints(player2.getLifePoints()+player2GodFavor.getEffect());
				}
			}
		}catch(Exception e) {
			print(e.getStackTrace());
		}
	}
	
	public static void resetPlayers() {
		player1.resetFavors();
		player2.resetFavors();
		player1.resetRolls();
		player2.resetRolls();
	}
	
	public static boolean TakeNames(String Arguments) {
		String[] ArgumentList = Arguments.split(";");
		String name1 = null;
		String name2 = null;
		try {			
			if(checkName(ArgumentList[0])&&checkName(ArgumentList[1])) {
				name1 = ArgumentList[0];
				name2 = ArgumentList[1];
			}else {
				return false;
			}
			Long LifePoints = Long.parseLong(ArgumentList[2]);
			if(LifePoints<=5) {
				LifePoints = 5l;
			}
			Short GodPower = Short.parseShort(ArgumentList[3]);
			player1 = new player(name1, LifePoints, GodPower);
			player2 = new player(name2, LifePoints, GodPower);
			turn = player1;
			return true;
		}catch(Exception e){
			print(e.getStackTrace());
			return false;
		}
	}
	public static boolean TakeRolls(String Arguments) {
		String[] ArgumentList = Arguments.split(";");
		int len = ArgumentList.length;
		String[] RollList = {"","","","","",""};
		Short GodPowerRoll = 0;
		if(len!=6) {
			println("Please enter all the rolls...");
			return false;
		}
		for(int i=0;i<len;i++) {
			String roll = ArgumentList[i];
			if(!Arrays.stream(dice.getRolls()).anyMatch(roll::equals)) {
				println("There is no "+roll+" roll. Please enter correctly...");
				return false;
			}
			if(roll.contains("G")) {
				if(!(++GodPowerRoll<5)) {
					println("GodPower roll may not exceed 4. Please enter correctly...");
					return false;
				}roll = roll.split("G")[1];
			}RollList[i] = roll;
		}
		turn.setRolls(RollList);
		turn.setGodPower(turn.getGodPower()+GodPowerRoll);
		return true;
	}
	
	public static boolean TakeGodFavor(String Arguments) {
		String[] ArgumentList = Arguments.split(";");
		String Favor = ArgumentList[0];
		byte level = Byte.parseByte(ArgumentList[1]);
		if(!Arrays.stream(godFavor.getFavors()).anyMatch(Favor::equals)) {
			println("God Favor doesn't exist...");
			return false;
		}else if(level>3||level<1) {
			println("God Favor level is not valid...");
			return false;
		}
		turn.setGodFavorSelected(Favor);
		turn.setGodFavorLevel(level);
		return true;
	}
	
	public static void printPlayers() {
		println(player1.show());
		println(player2.show());
	}
	
	
	public static void end() {
		in.close();
//		print("----------------------------\nProgram Ended\n----------------------------");
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String UserInput1;
		String command;
		String Arguments;
		while(true) {
			UserInput1 = input("> ").strip();
			if(UserInput1.equals("quit")) {
				break;
			}
			if(UserInput1.contains(" ")) {
				String[] InputSplit = UserInput1.split(" ");
				int len = InputSplit.length;
				command = InputSplit[len-2];
				Arguments = InputSplit[len-1];
				executeCommand(command, Arguments);
			}else {
				command = UserInput1;
				executeCommand(command);
			}
		}
		// Ending the script
		end();
	}
}
