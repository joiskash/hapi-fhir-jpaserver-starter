package ca.uhn.fhir.jpa.starter;

import lombok.Data;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;

@Data
@Component
@ConfigurationProperties(prefix = "tus-server")
public class TusServerProperties {

	private String fileDirectory;

	private Long maxSize;

	private String contextPath;
}
