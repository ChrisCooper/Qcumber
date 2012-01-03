//
//  Course.h
//  Qcumber
//
//  Created by Chris Cooper on 11-12-31.
//  Copyright (c) 2011 __MyCompanyName__. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "Subject.h"

@interface Course : NSObject

@property (strong) NSString *title;
@property (strong) NSString *descr;
@property (strong) NSString *number;

@property (strong) NSArray *sections;
@property (strong) Subject *subject;

@end
