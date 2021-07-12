package ubb.config;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration
@ComponentScan({"ubb.service",
        "ubb.repository",
        "ubb.domain",
        "ubb.ui"})

public class CatalogConfig {
}
