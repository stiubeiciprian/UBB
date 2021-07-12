package ubb.core.service;

import ubb.core.model.Pod;

import java.util.List;

public interface PodServiceInterface {
    Pod add(String name, Integer cost);

    List<Pod> getPods();

    //returns all pods which are currently not scheduled on any node.
    List<Pod> getAvailablePods();

    Pod delete(Long podId);

}
