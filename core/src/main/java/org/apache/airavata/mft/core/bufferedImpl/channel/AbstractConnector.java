/*
 *   Licensed to the Apache Software Foundation (ASF) under one
 *   or more contributor license agreements.  See the NOTICE file
 *   distributed with this work for additional information
 *   regarding copyright ownership.  The ASF licenses this file
 *   to you under the Apache License, Version 2.0 (the
 *   "License"); you may not use this file except in compliance
 *   with the License.  You may obtain a copy of the License at
 *
 *  http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing,
 *  software distributed under the License is distributed on an
 *   "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 *   KIND, either express or implied.  See the License for the
 *   specific language governing permissions and limitations
 *   under the License.
 */

package org.apache.airavata.mft.core.bufferedImpl.channel;

import org.apache.airavata.mft.core.api.Connector;
import org.apache.airavata.mft.core.api.ConnectorChannel;
import org.apache.airavata.mft.core.api.SinkConnector;
import org.apache.airavata.mft.core.api.SourceConnector;
import org.apache.airavata.mft.core.bufferedImpl.ConnectorException;

import java.io.IOException;


/**
 * Common class for {@link SinkConnector} and {@link SourceConnector} implementations
 * This overrides closeChannel method and release all resources allocated to releasing channel
 */
public abstract class AbstractConnector implements Connector {

    @Override
    public void closeChannel(ConnectorChannel channel) throws ConnectorException {

        try {
            channel.closeChannel();

        } catch (IOException e) {
            throw new ConnectorException("Error occurred while closing stream", e);
        }

    }

}
