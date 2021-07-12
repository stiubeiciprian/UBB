package ubb.core.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.repository.NoRepositoryBean;
import ubb.core.model.BaseEntity;

import javax.transaction.Transactional;
import java.io.Serializable;

@NoRepositoryBean
@Transactional
public interface CloudAppRepository<T extends BaseEntity<ID>, ID extends Serializable> extends JpaRepository<T, ID> {
}
