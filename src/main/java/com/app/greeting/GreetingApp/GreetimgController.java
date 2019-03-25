package com.app.greeting.GreetingApp;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class GreetimgController {
	
	@RequestMapping("/gtGreeting")
	public String getGreeting() {
		
		return "Hello AWS";
	}

}
