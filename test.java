import java.util.ArrayList; // import the ArrayList class
import java.util.HashMap; // import the HashMap class
import java.util.Scanner;

interface OverWatch { // 인터페이스
	void name(); // 추상 메소드
	void lClick(); // 추상 메소드
	void rClick(); // 추상 메소드
	void shiftButton(); // 추상 메소드
	void eButton(); // 추상 메소드
	void qButton(); // 추상 메소드
}

class Mei implements OverWatch { // 인터페이스 구현 클래스
	public void name() { // 오버라이딩
		System.out.println("이름 : 메이");
	}
	public void lClick() { // 오버라이딩
	}
	public void rClick() { // 오버라이딩
		System.out.println("우클릭 : 고드름 투사체");
	}
	public void shiftButton() { // 오버라이딩
		System.out.println("shift : 급속 빙결");
	}
	public void eButton() { // 오버라이딩
		System.out.println("e : 빙벽");
	}
	public void qButton() { // 오버라이딩
		System.out.println("q : 눈보라(궁극기)");
	}
}

public class test{
  public static void main(String [] args){
    OverWatch ow; // 인터페이스 객체 선언
    ow = new Mei(); // 업캐스팅
    ow.name();

  }
}
