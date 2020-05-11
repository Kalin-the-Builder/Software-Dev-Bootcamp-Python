package net.codejava;

public class Person {
	//Variables|Attributes
	String name;
	String phoneNum;
	String emailAddress;
	String physicalAddress;
	String workType;
	
	//Constructors
	public Person(String workType,String name,String phoneNum,String emailAddress,String physicalAddress) {
		this.workType = workType;
		this.name = name;
		this.phoneNum = phoneNum;
		this.emailAddress = emailAddress;
		this.physicalAddress = physicalAddress;
	}
	//Methods
	public String toString() {
		String output = "\n" + workType;
		output += "\nName: " + name;
		output += "\nPhone Number: " + phoneNum;
		output += "\nEmail Address: " + emailAddress;
		output += "\nPhysical Address: " + physicalAddress;
		
		return output;
	}
}
