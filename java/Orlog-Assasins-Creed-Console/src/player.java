
public class player {
	private String Name;
	private long LifePoints;
	private int GodPower;
	private String[] Rolls;
	private String GodFavorSelected = "";
	private byte GodFavorLevel = 0;
	private int MeleeAttack;
	private int MeleeDefense;
	private int RangeAttack;
	private int RangeDefense;
	private int Steal;

	// Constructor
	public player(String name, long lifePoints, short godPower) {
		super();
		Name = name;
		LifePoints = lifePoints;
		GodPower = godPower;
	}
	
	// Getter and Setters
	
	public String getGodFavorSelected() {
		return GodFavorSelected;
	}
	
	public int getMeleeAttack() {
		return MeleeAttack;
	}

	public void setMeleeAttack(int meleeAttack) {
		MeleeAttack = meleeAttack;
	}

	public int getMeleeDefense() {
		return MeleeDefense;
	}

	public void setMeleeDefense(int meleeDefense) {
		MeleeDefense = meleeDefense;
	}

	public int getRangeAttack() {
		return RangeAttack;
	}

	public void setRangeAttack(int rangeAttack) {
		RangeAttack = rangeAttack;
	}

	public int getRangeDefense() {
		return RangeDefense;
	}

	public void setRangeDefense(int rangeDefense) {
		RangeDefense = rangeDefense;
	}

	public int getSteal() {
		return Steal;
	}

	public void setSteal(int steal) {
		Steal = steal;
	}

	public void setGodFavorSelected(String godFavorSelected) {
		GodFavorSelected = godFavorSelected;
	}
	
	public byte getGodFavorLevel() {
		return GodFavorLevel;
	}
	
	public void setGodFavorLevel(byte godFavorLevel) {
		GodFavorLevel = godFavorLevel;
	}
	public String getName() {
		return Name;
	}
	public String[] getRolls() {
		return Rolls;
	}

	public void setRolls(String[] rolls) {
		Rolls = rolls;
	}

	public void setName(String name) {
		Name = name;
	}
	public long getLifePoints() {
		return LifePoints;
	}
	public void setLifePoints(long lifePoints) {
		LifePoints = lifePoints;
	}
	public int getGodPower() {
		return GodPower;
	}
	public void setGodPower(int i) {
		GodPower = i;
	}
	
	// other functions
	public String show() {
		return this.Name+";"+this.LifePoints+";"+this.GodPower;
	}
	public void UseRoll() {
		for(String Roll: Rolls) {
			if(Roll.equals("MA")) {
				MeleeAttack++;
			}else if(Roll.equals("MD")) {
				MeleeDefense++;
			}else if(Roll.equals("RA")) {
				RangeAttack++;
			}else if(Roll.equals("RD")) {
				RangeDefense++;
			}else if(Roll.equals("ST")) {
				Steal++;
			}
		}
	}
	public void resetRolls() {
		Rolls = null;
		MeleeAttack = 0;
		MeleeDefense = 0;
		RangeAttack = 0;
		RangeDefense = 0;
		Steal = 0;
	}
	public void resetFavors() {
		GodFavorSelected = "";
		GodFavorLevel = 0;
	}
}
