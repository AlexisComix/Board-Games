
public class godFavor {
	private static final String[] Favors = {"TS", "TT", "IR"};
	private String Name;
	private int Level;
	private int Cost;
	private int Effect;
	
	public godFavor(String name, int level) {
		super();
		if(name.equals("TS")) {
			Cost = level*4;
			Effect = -1+level*3;
		}else if(name.equals("TT")) {
			Cost = level*3;
			Effect = level;
		}else if(name.equals("IR")) {
			Cost = 1+level*3;
			Effect = level*2;
		}
		Name = name;
		Level = level;
	}
	
	public int getCost() {
		return Cost;
	}
	public int getEffect() {
		return Effect;
	}
	public String getName() {
		return Name;
	}
	public int getLevel() {
		return Level;
	}
	public static String[] getFavors() {
		return Favors;
	}
	
}
